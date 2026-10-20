"""One current framework release identifier; research and schema versions stay separate."""
import re
from pathlib import Path
from ..core import repository as r

MANIFEST = 'framework/export-manifest.json'
RELEASE = re.compile(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)')
ID = 'acme'


def validate_manifest(manifest):
    r.require(isinstance(manifest, dict), 'Invalid export manifest.')
    value = manifest.get('framework_version')
    r.require(isinstance(value, str) and RELEASE.fullmatch(value) is not None,
              'framework_version must use MAJOR.MINOR.PATCH without leading zeros.')
    if 'framework_id' in manifest or 'framework_name' in manifest:
        r.require(manifest.get('framework_id') == 'acme' and manifest.get('framework_name') == 'Autonomous and Collaborative Mathematical Exploration',
                  'Installed framework identity must be ACME / Autonomous and Collaborative Mathematical Exploration.')
    return value


def installed(root):
    """Lightweight identity of the installed ACME framework, or None when absent.

    Discovery catalogs carry this identity (no fingerprints) so intake routing
    can recognize ACME-lineage material."""
    path = r.safe_path(Path(root), MANIFEST)
    if not path.exists():
        return None
    manifest = r.read_json(path)
    validate_manifest(manifest)
    if manifest.get('framework_id') != ID:
        return None
    return {'framework_id': ID, 'framework_version': manifest['framework_version']}


def validate_context(value):
    """A recorded framework stamp keeps its format; it is an import/export marker only."""
    r.require(isinstance(value, dict) and isinstance(value.get('framework_id'), str) and
              re.fullmatch(r'[a-z][a-z0-9-]*', value['framework_id']), 'Invalid framework identity.')
    validate_manifest({'framework_version': value.get('framework_version')})


def validate_stamps(record):
    """Records may omit framework stamps; a present stamp keeps its format."""
    value = record.get('framework')
    if value is not None:
        validate_context(value)


def check(root, reader=None):
    # Bare record-engine repositories need not install the exportable framework.
    # Submitted trees supply their own reader; unstaged files cannot repair them.
    try:
        if reader is None:
            path = r.safe_path(Path(root), MANIFEST)
            if not path.exists():
                r.require(not (Path(root) / 'framework/readme.md').exists() and
                          not (Path(root) / 'scripts/export-framework.py').exists(),
                          'Installed framework is missing its export manifest.')
                return []
            manifest = r.read_json(path)
        else:
            manifest = reader(MANIFEST)
        validate_manifest(manifest)
        # Layer 5: the review-compatibility policy is a lazy file. It is no
        # longer read here; only the export manifest is validated.
        return []
    except (OSError, ValueError, KeyError, TypeError) as error:
        return ['Framework version: ' + str(error)]
