"""Shared necessary material locator checks, independent of storage schemas."""
from ..core import repository as r
from ..core import paths as public_paths


def read_material(repo, path, material_data=None):
    if material_data is not None and path in material_data:
        return material_data[path]
    if hasattr(repo, 'selected_tree'):
        return repo.selected_tree.bytes(path)
    return r.read_bytes(r.safe_path(repo.root, path), root=repo.root)


def visible_markdown(text):
    """Compatibility entry point for the shared Markdown block parser."""
    from ..core import links as research_links
    return research_links.visible_markdown(text)


def validate_locator_targets(locators, read, paths=()):
    """Check explicit locators through a text/bytes reader, without a store schema."""
    from ..core import links as research_links
    data = {}
    for path in paths:
        public_paths.check_public_target(path)
        data[path] = read(path)
    anchors = {}
    for item in locators:
        path = item['path']
        public_paths.check_public_target(path)
        if path not in data:
            data[path] = read(path)
        if item.get('anchor') and path.lower().endswith('.md'):
            if path not in anchors:
                text = data[path].decode('utf-8-sig') if isinstance(data[path], bytes) else data[path]
                anchors[path] = research_links.anchor_occurrences(text)
            r.require(anchors[path][item['anchor']] == 1,
                      'Received required anchor missing: ' + path + '#' + item['anchor']
                      if not anchors[path][item['anchor']] else 'Received required anchor ambiguous: ' + path + '#' + item['anchor'])


def validate_locators(repo, locators, paths=(), material_data=None):
    """Check declared local files/anchors, without judging bytes or mathematics."""
    validate_locator_targets(locators, lambda path: read_material(repo, path, material_data), paths)


def _navigation_path(root, owner, path, planned):
    # Only this explicitly selected private file's internal navigation retains
    # its owning context. Other private targets stay barred before any access.
    if path != owner or not public_paths.private_file(owner):
        public_paths.check_public_target(path)
    if public_paths.in_pdf_store(path):
        # Generic logical source navigation never resolves the mount.
        return None
    root = public_paths.resolved_path(root)
    located = public_paths.ordinary_path(root, path)
    # Only necessary in-repository ancestors must already be directories or
    # remain absent for the selected files to create during publication.
    parent = root
    for part in located.relative_to(root).parts[:-1]:
        parent /= part
        relative = parent.relative_to(root).as_posix()
        r.require(relative not in planned and (not parent.exists() or parent.is_dir()),
                  'Required navigation directory is occupied by a file: ' + relative)
    # Only actual selected file paths supply these structural parent facts.
    # A component boundary keeps an unrelated similarly named sibling out.
    pending_parent = any(name.startswith(path + '/') for name in planned)
    if pending_parent:
        r.require(path not in planned and (not located.exists() or located.is_dir()),
                  'Required navigation directory is occupied by a file: ' + path)
        return located, True
    if path in planned:
        return located, False
    if not located.exists():
        raise FileNotFoundError('Referenced local target is missing: ' + path)
    return located, located.is_dir()


def validate_navigation_targets(root, owner, locators, read, *, planned=()):
    """Validate body links and return their read-free publication guard."""
    from ..core import links
    locators, directory_anchors = tuple(locators), set()
    for item in locators:
        path, anchor = item['path'], item.get('anchor', '')
        target = _navigation_path(root, owner, path, planned)
        if target is None:
            continue
        _located, directory = target
        if directory:
            if anchor and path.lower().endswith('.md'):
                directory_anchors.add(path)
            continue
        if anchor and path.lower().endswith('.md'):
            raw = read(path)
            text = raw.decode('utf-8-sig') if isinstance(raw, bytes) else raw
            r.require(links.anchor_occurrences(text)[anchor] == 1,
                      'Referenced Markdown anchor is missing or ambiguous: ' + path + '#' + anchor)

    def recheck():
        for item in locators:
            path = item['path']
            target = _navigation_path(root, owner, path, planned)
            if path in directory_anchors and path not in planned:
                r.require(target is not None and target[1], 'Selected navigation target changed from a directory: ' + path)
    return recheck

