"""Explicit Task coordination and the invariant type of a numbered T family."""
from . import documents, identity
from ..core import links, source_refs

require = identity.require


def declarations(path, body):
    sections = body.sections('Task coordination')
    require(len(sections) <= 1, 'A Task has at most one Task coordination section.')
    fields = {}
    for cells, _ in sections[0][0].table(('Field', 'Value')) if sections else ():
        key, value = cells
        require(key in {'task-type', 'joint-task'} and key not in fields,
                'Unknown or repeated Task coordination field: ' + key)
        fields[key] = value
    require('task-type' not in fields or fields['task-type'] == 'joint',
            'The optional task-type declaration is joint; absence means ordinary.')
    kind = fields.get('task-type', 'ordinary')
    parent = documents.locator(path, fields['joint-task']) if 'joint-task' in fields else None
    require(kind != 'joint' or parent is None, 'A joint Task cannot have a joint parent.')
    return kind, parent


def contracts(document):
    return {loc.anchor for decision in document.decisions.values()
            for role, loc, _ in decision.relations
            if role == 'contract' and loc.path == document.path}


def validate(document, read, *, paths=(), previous=()):
    if document.identity.kind != 'T':
        return
    family = [document]
    for path in paths:
        if path != document.path and identity.in_namespace(path, family=document.identity):
            family.append(documents.parse(path, read(path)))
    family.extend(previous)
    require(all(doc.task_type == document.task_type for doc in family),
            'Task family type is invariant; every joint version declares task-type joint.')
    require(not document.identity.source_repository or document.task_type == 'joint',
            'Only a necessary joint contract can be received as an external Task.')
    parent = document.joint_task
    if parent:
        require(not source_refs.external(parent.path), 'A joint parent must be an actual contract in this repository.')
        ident = identity.parse(parent.path)
        require(ident.kind == 'T' and ident.family != document.identity.family,
                'A joint parent must be a different numbered T family.')
        target = documents.parse(parent.path, read(parent.path))
        require(target.task_type == 'joint' and target.joint_task is None,
                'The exact parent must be a joint Task without a parent.')
        require(parent.anchor in contracts(target) and links.anchor_occurrences(target.text)[parent.anchor] == 1,
                'The joint parent must name an exact fixed contract anchor.')
        validate(target, read, paths=paths)
