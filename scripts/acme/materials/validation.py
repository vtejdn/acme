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
                anchors[path] = research_links.anchors_text(text)
            r.require(item['anchor'] in anchors[path],
                      'Received required anchor missing: ' + path + '#' + item['anchor'])


def validate_locators(repo, locators, paths=(), material_data=None):
    """Check declared local files/anchors, without judging bytes or mathematics."""
    validate_locator_targets(locators, lambda path: read_material(repo, path, material_data), paths)

