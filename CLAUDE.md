# CLAUDE.md — gha repository

This is a collection of reusable composite GitHub Actions maintained by iMio for CI/CD automation.

## Repository structure

Each action lives in its own top-level directory containing a single `action.yml`. There are no compiled artifacts, build scripts, or test suites — everything is YAML.

```
<action-name>/
  action.yml       # composite action definition
```

`event.json` at the root is used for local testing with `act`.

## Actions inventory

| Directory | Description |
|-----------|-------------|
| `build-push-notify` | Build and push Docker image to registry, notify on Mattermost |
| `check-url-availibility` | Poll until a URL becomes available |
| `code-analysis-notify` | Run code analysis and notify on Mattermost |
| `deb-build-push-notify` | Build a Debian package, push to apt repo, notify on Mattermost |
| `helm-release-notify` | Release a Helm chart and notify on Mattermost |
| `helm-test-notify` | Lint and test a Helm chart and notify on Mattermost |
| `k8s-update-tag` | Update a component tag in a Kubernetes values file and push the commit |
| `mattermost-notify` | Send a notification to a Mattermost webhook (used by other actions) |
| `plone-package-test-notify` | Run Plone package tests (via buildout/uv) and notify on Mattermost |
| `plone-theme-build-push-notify` | Upload a Plone theme to a site, notify on Mattermost |
| `repository-dispatch-notify` | Trigger a repository dispatch event, optionally notify on Mattermost |
| `rundeck-notify` | Call a Rundeck job and notify on Mattermost |
| `tag-notify` | Re-tag a Docker image in a registry and notify on Mattermost |

## Cross-action dependencies

`plone-theme-build-push-notify` and `repository-dispatch-notify` call `mattermost-notify` internally. When modifying `mattermost-notify` inputs, check both callers.

## Release process

1. Update `CHANGELOG.md` with a new `## [vX.Y.Z] - YYYY-MM-DD` section.
2. Commit: `git commit -am "doc: Release vX.Y.Z"`
3. Tag and push: `git tag vX.Y.Z && git push --follow-tags`

The `.github/workflows/release.yml` workflow triggers on `v*` tags. It:
- Extracts the changelog section for the tag and creates a GitHub release.
- Force-updates the major version tag (e.g. `v5`) to point to the new patch release.

Callers reference actions as `imio/gha/<action-name>@v5` (major tag) or a full version like `@v5.1.0`.

## Local testing with `act`

```bash
act -e event.json
```

`event.json` at the repo root provides the simulated GitHub event payload.
