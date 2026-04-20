# Aistra Tools

## Purpose

`Aistra/tools/` is the repo-local subtools layer for Aistra.

It owns package-local scripts, audits, scoring helpers, and current ops
workflows. It follows the workspace parent `Tools/` framework while remaining
locally scoped to Aistra's routes and package controls.

## Current contents

- audit scripts for current surfaces, claims, file registry, minimality, and root budget
- route-1 helpers for packet generation, scoring, ops runs, and prediction conversion

## Boundary

This layer may automate bounded package operations, but it does not define
package truth. Canonical package posture still belongs to Aistra's front door
and governance surfaces.

## Minimum entry rule

Use this file plus `../governance/AUTHORITATIVE_INDEX_v0_1.md` before treating
any Aistra tool output as current package state.

## Status

`aistra repo-local subtools layer`
