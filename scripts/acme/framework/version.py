"""One current framework release identifier; research and schema versions stay separate."""
from datetime import date, datetime, timezone
import json
import re
import time
import uuid
from pathlib import Path
from urllib import request
from ..core import repository as r

VERSION_FILE = 'framework/version.json'
RELEASE = re.compile(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)')
OFFICIAL_REPOSITORY = 'https://github.com/vtejdn/acme'
OFFICIAL_REF = 'main'
OFFICIAL_VERSION_URL = (OFFICIAL_REPOSITORY.replace('https://github.com/',
                         'https://raw.githubusercontent.com/', 1) + '/' +
                         OFFICIAL_REF + '/' + VERSION_FILE)
UPDATE_CACHE = 'repository/framework-update-check.json'
UPDATE_CLAIM = '.tmp/framework-update-request.json'
UPDATE_TIMEOUT = 10.0
UPDATE_MAX_BYTES = 256 * 1024
UPDATE_LOCK_TIMEOUT = 2.0
UPDATE_FIELDS = {'last_attempt_on', 'result', 'latest_version', 'notified_version'}


def validate_metadata(metadata):
    r.require(isinstance(metadata, dict) and set(metadata) == {'framework_version'},
              'Framework version metadata must contain only framework_version.')
    value = metadata['framework_version']
    r.require(isinstance(value, str) and RELEASE.fullmatch(value) is not None,
              'framework_version must use MAJOR.MINOR.PATCH without leading zeros.')
    return value


def installed(root):
    """Read the installed release metadata, or None when absent."""
    path = r.safe_path(Path(root), VERSION_FILE)
    if not path.exists():
        return None
    metadata = r.read_json(path)
    validate_metadata(metadata)
    return metadata


def check(root, reader=None):
    # Bare record-engine repositories need not install the common framework.
    # Submitted trees supply their own reader; unstaged files cannot repair them.
    try:
        if reader is None:
            path = r.safe_path(Path(root), VERSION_FILE)
            if not path.exists():
                r.require(not (Path(root) / 'framework/readme.md').exists(),
                          'Installed framework is missing framework/version.json.')
                return []
            metadata = r.read_json(path)
        else:
            metadata = reader(VERSION_FILE)
        validate_metadata(metadata)
        return []
    except (OSError, ValueError, KeyError, TypeError) as error:
        return ['Framework version: ' + str(error)]


def release_tuple(value):
    """Compare the declared three integers, without lexical version ordering."""
    validate_metadata({'framework_version': value})
    return tuple(int(part) for part in value.split('.'))


def update_cache(root):
    """A malformed disposable cache is unchecked, rather than configuration."""
    try:
        cache = r.read_json(r.safe_path(root, UPDATE_CACHE), root=root)
        r.require(isinstance(cache, dict) and set(cache) == UPDATE_FIELDS,
                  'Invalid framework update cache fields.')
        day = cache['last_attempt_on']
        r.require(isinstance(day, str) and date.fromisoformat(day).isoformat() == day,
                  'Invalid framework update cache day.')
        r.require(cache['result'] in ('success', 'unavailable'), 'Invalid cached result.')
        if cache['result'] == 'success':
            release_tuple(cache['latest_version'])
        else:
            r.require(cache['latest_version'] is None, 'Unavailable cache has no fresh version.')
        if cache['notified_version'] is not None:
            release_tuple(cache['notified_version'])
        return cache
    except (OSError, ValueError, KeyError, TypeError):
        return None


class _NoUpdateRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # A redirect must not turn a metadata check into another retrieval.
        return None


def read_official_version(*, opener=None, monotonic=None):
    """One bounded public GET; return bytes without installing framework files."""
    clock = monotonic or time.monotonic
    started = clock()
    open_url = opener or request.build_opener(_NoUpdateRedirect()).open
    query = request.Request(OFFICIAL_VERSION_URL, method='GET', headers={
        'Accept': 'application/json', 'Accept-Encoding': 'identity',
        'User-Agent': 'ACME-framework-version-check'})
    with open_url(query, timeout=UPDATE_TIMEOUT) as response:
        r.require(response.geturl() == OFFICIAL_VERSION_URL,
                  'Official version response changed the requested URL.')
        r.require(response.status == 200, 'Official version response was not HTTP 200.')
        r.require(response.headers.get('Content-Encoding', 'identity').lower() == 'identity',
                  'Official version response must not be compressed.')
        length = response.headers.get('Content-Length')
        if length is not None:
            r.require(length.isdecimal() and int(length) <= UPDATE_MAX_BYTES,
                      'Official version metadata exceeds the response size limit.')
        chunks, size = [], 0
        # HTTPResponse.read1 returns one available block, so the elapsed budget
        # is checked between blocks instead of accumulating an unbounded body.
        while True:
            r.require(clock() - started < UPDATE_TIMEOUT,
                      'Official version request exceeded its time budget.')
            block = response.read1(min(16384, UPDATE_MAX_BYTES + 1 - size))
            r.require(clock() - started < UPDATE_TIMEOUT,
                      'Official version request exceeded its time budget.')
            if not block:
                break
            size += len(block)
            r.require(size <= UPDATE_MAX_BYTES, 'Official version metadata exceeds the response size limit.')
            chunks.append(block)
        return b''.join(chunks)


def _official_version(data):
    metadata = json.loads(data.decode('utf-8-sig'))
    return validate_metadata(metadata)


def _update_result(local, cache=None, *, status=None, attempted=False,
                   reused=False, saved=None, **diagnostics):
    facts = cache or dict.fromkeys(UPDATE_FIELDS)
    newer = (facts['result'] == 'success' and local is not None and
             release_tuple(facts['latest_version']) > release_tuple(local))
    return {**facts, 'status': status or facts['result'], 'attempted': attempted,
            'cache_reused': reused, 'cache_saved': saved, 'installed_version': local,
            'official_repository': OFFICIAL_REPOSITORY,
            'reminder_due': bool(newer and facts['latest_version'] != facts['notified_version']
                                 and status not in ('disabled', 'offline')),
            **diagnostics}


def check_update(root, *, force=False, offline=False, now=None, fetch=None):
    """Explicit start-of-work metadata query; no actor, Git, research or upgrade."""
    root = Path(root).resolve()
    local = None
    try:
        config = r.read_json(r.safe_path(root, 'repository/config.json'), root=root)
        r.require(isinstance(config, dict), 'Repository configuration must be an object.')
        enabled = config.get('framework_update_check', True)
        r.require(type(enabled) is bool, 'framework_update_check must be a Boolean.')
    except (OSError, ValueError, KeyError, TypeError) as error:
        return _update_result(None, status='configuration-error', error=str(error))
    try:
        metadata = installed(root)
        r.require(metadata is not None, 'Installed framework/version.json is missing.')
        local = metadata['framework_version']
        cache = update_cache(root)
        if not enabled or offline:
            return _update_result(local, cache, status='disabled' if not enabled else 'offline')
        r.require(now is None or (isinstance(now, datetime) and now.utcoffset() is not None),
                  'The update clock must supply an aware datetime.')
        with r.locked(root, timeout=UPDATE_LOCK_TIMEOUT):
            instant = now or datetime.now(timezone.utc)
            today = instant.astimezone(timezone.utc).date().isoformat()
            # Reread after the lock: another responsible agent may have claimed
            # this day while this caller was waiting.
            cache = update_cache(root)
            if cache is not None and cache['last_attempt_on'] > today:
                return _update_result(local, cache, status='superseded', saved=False)
            if cache is not None and cache['last_attempt_on'] == today and not force:
                return _update_result(local, cache, reused=True, saved=True)
            claim = {'last_attempt_on': today, 'result': 'unavailable',
                     'latest_version': None,
                     'notified_version': cache['notified_version'] if cache else None}
            r.write_json(root / UPDATE_CACHE, claim, root=root)
            owner = uuid.uuid4().hex
            request_claim = r.safe_path(root, UPDATE_CLAIM)
            r.write_json(request_claim, {'owner': owner}, root=root)
    except (OSError, ValueError, KeyError, TypeError) as error:
        return _update_result(local, status='local-error', cache_error=str(error), saved=False)
    # The claim is already a complete unavailable result. Interruption, even
    # before publication, cannot leave partial JSON or a false success.
    outcome, diagnostics = dict(claim), {}
    try:
        outcome['latest_version'] = _official_version((fetch or read_official_version)())
        outcome['result'] = 'success'
    except Exception as error:
        diagnostics['error'] = str(error)
    try:
        with r.locked(root, timeout=UPDATE_LOCK_TIMEOUT):
            try:
                current = update_cache(root)
                if (_request_owner(root) != owner or current is None or current['last_attempt_on'] != today or
                        current['result'] != 'unavailable' or current['latest_version'] is not None):
                    # Equal cache bytes do not identify a request. A completed
                    # later failure has released its owner just like a success.
                    return _update_result(local, current, status='superseded', attempted=True,
                                          saved=False, **diagnostics)
                outcome['notified_version'] = current['notified_version']
                r.write_json(root / UPDATE_CACHE, outcome, root=root)
                return _update_result(local, outcome, attempted=True, saved=True, **diagnostics)
            finally:
                if _request_owner(root) == owner:
                    r.unlink(request_claim, root=root)
    except (OSError, ValueError, KeyError, TypeError) as error:
        return _update_result(local, outcome, attempted=True, saved=False,
                              cache_error=str(error), **diagnostics)


def _request_owner(root):
    try:
        claim = r.read_json(r.safe_path(root, UPDATE_CLAIM), root=root)
        r.require(isinstance(claim, dict) and isinstance(claim.get('owner'), str), 'Invalid temporary request owner.')
        return claim['owner']
    except FileNotFoundError:
        return None


def record_update_notification(root, value, *, expected_notified_version):
    """Record an actual reminder only while its observed notification fact holds."""
    root = Path(root).resolve()
    release_tuple(value)
    if expected_notified_version is not None:
        release_tuple(expected_notified_version)
    local = installed(root)
    r.require(local is not None and release_tuple(value) > release_tuple(local['framework_version']),
              'An upgrade reminder must name a newer version than the installed framework.')
    with r.locked(root, timeout=UPDATE_LOCK_TIMEOUT):
        current = update_cache(root)
        r.require(current is not None, 'No current framework update cache can retain the notification fact.')
        if current['notified_version'] != expected_notified_version:
            return {'notified_version': current['notified_version'], 'cache_saved': False,
                    'status': 'superseded'}
        current['notified_version'] = value
        r.write_json(root / UPDATE_CACHE, current, root=root)
    return {'notified_version': value, 'cache_saved': True}
