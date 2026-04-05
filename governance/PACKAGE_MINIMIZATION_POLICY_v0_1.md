# Package Minimization Policy

## Purpose

This package should resist silent file sprawl. Every file must justify its existence, and the root folder must stay intentionally small.

## Core rule

A file may exist only if all four conditions hold:

1. it serves a distinct operational, validation, governance, or handoff role;
2. that role is not already covered by an existing file;
3. its likely reader and entry path are clear;
4. its location is the shallowest one that preserves clarity without inflating the root.

If any condition fails, the file should be merged, moved, or deleted.

## Root budget rule

The package root is reserved for a narrow allowlist of front-door and machine-anchor surfaces.

Allowed root roles:
- one package overview
- one primary start surface
- one current status surface
- one current execution-order surface
- one main operational guide
- one operator quickstart
- one verification summary
- one changelog
- one authoritative index
- one integrity manifest
- one compact state summary
- essential runtime/program files that are still retained for backward compatibility

Everything else should prefer a subdirectory.

## New-file admission test

Before adding a file, answer all of these:

- What exact job does it do?
- Why can no current file absorb that job?
- Who reads it first?
- Why does it belong in this directory rather than a deeper one?
- What existing file becomes removable once this is added?

If you cannot answer all five cleanly, do not add the file.

## Anti-bloat constraints

- Do not create a new root markdown file for a one-off memo.
- Do not create version-suffixed siblings unless content is materially different and both versions must coexist.
- Do not keep historical drafts at root.
- Prefer appending to changelog, status, or audit surfaces over creating another summary.
- Prefer generated artifacts under `reports/generated/` or another non-canonical run directory.
- Prefer governance rules under `governance/`.

## Enforcement

Use:
- `governance/ROOT_ALLOWLIST_v0_1.json`
- `governance/FILE_JUSTIFICATION_REGISTRY_v0_1.json`
- `tools/audit_root_budget.py`

A package change should fail review if it adds an unregistered root file or leaves a file without a justification entry.

## Repo-wide registry rule
Root control is not enough. Every shipped file must appear in `REPOSITORY_FILE_REGISTRY_v0_1.json` with a role and justification, and the repository audit must fail if any file is missing from that registry.
