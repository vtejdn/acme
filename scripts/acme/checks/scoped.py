"""Read explicitly selected public identity and source-reference fields."""
from pathlib import Path
import re
from ..core import repository as r
from ..materials import identity as names, documents


def view_for(tree):
    view = tree.research_view()
    view.selected_tree = tree
    view.read_document = lambda path: r.json_from(view, path)
    return view


def external_references(tree, selections):
    """Check explicit path-to-field selections using this Git view's readers."""
    from ..core import external, source_refs
    r.require(isinstance(selections, dict), 'Select external-reference paths and their fields explicitly.')
    view = view_for(tree)
    checked, files = [], set()

    def field(owner, label, operation, *args):
        try: value = operation(*args)
        except (ValueError, KeyError, IndexError, TypeError) as error:
            raise ValueError(owner + ':' + label + ': ' + str(error)) from error
        return value

    def provenance(value, label):
        if label == 'transport.repository': return value['transport']['repository'], None
        match = re.fullmatch(r'items\[(0|[1-9][0-9]*)\]\.source\.(repository|author)', label)
        r.require(match is not None, 'Unsupported intake reference field: ' + label)
        item = value['items'][int(match[1])]
        if match[2] == 'repository': return item['source']['repository'], None
        if match[2] == 'author':
            r.require(item['kind'] in {'C', 'T', 'R', 'L', 'J'}, 'This item kind has no external author field.')
            source = item['source']
            r.require(isinstance(source['author_name'], str) and source['author_name'].strip(),
                      'source.author_name needs the qualified original name.')
            return source['repository'], (source['author'], source['author_name'])

    for path, selected in selections.items():
        r.require(isinstance(path, str) and isinstance(selected, (list, tuple, set)) and selected
                  and all(isinstance(label, str) for label in selected) and len(selected) == len(set(selected)),
                  'Select a path and distinct nonempty reference fields.')
        r.paths.check_public_target(path)
        r.require(not r.paths.protected_path(Path(path)) and not r.paths.in_pdf_store(path),
                  'Selected reference is not a public material path: ' + path)
        if path.endswith('.md'):
            r.require(set(selected) == {'identity'}, path + ': choose the explicit identity field.')
            raw = tree.header(path)
            if 'identity' in selected:
                ident, values, _ = field(path, 'identity', documents.author_header, path, raw)
                if ident.source_repository:
                    field(path, 'source_repository', external.repository, view, ident.source_repository)
                    if ident.kind in 'CTRLJ':
                        original = names.parse(values['source_material']) if 'source_material' in values else None
                        field(path, 'author/source_material', external.person,
                              view, ident.author, ident.source_repository, original.author if original else None)
                checked.append({'path': path, 'field': 'identity'})
        elif re.fullmatch(r'intake/[^/]+/[^/]+\.json', path):
            value = field(path, 'JSON', tree.json, path)
            for label in sorted(selected):
                source, author = field(path, label, provenance, value, label)
                field(path, label, external.repository, view, source)
                if author is not None: field(path, label, external.person, view, author[0], source, author[1])
                checked.append({'path': path, 'field': label})
        else:
            raise ValueError(path + ': select public Markdown or an intake operation.')
        files.add(path)
    return {'files': len(files), 'fields': len(checked), 'checked': checked}
