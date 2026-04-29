# Contributing to OpenAZV Goods Ecosystem

## Branching

- Feature branches: `feat/<short-name>`
- Fix branches: `fix/<short-name>`
- Docs branches: `docs/<short-name>`

## Commit Style

Use concise imperative messages:
- `Add order event schema`
- `Define incident escalation policy`

## RFC-first for behavior changes

Before changing runtime behavior, open an RFC issue containing:
1. Problem statement.
2. Proposed API/event changes.
3. Compatibility and migration notes.
4. Security/compliance impact.

## Pull Request Checklist

- [ ] Domain event names follow `<bounded_context>.<entity>.<action>`.
- [ ] New agents include trigger events and ownership.
- [ ] Security and compliance implications are documented.
- [ ] Auditability requirements are defined where needed.
