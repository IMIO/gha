# iMio github actions

[![GitHub Release](https://img.shields.io/github/v/release/IMIO/gha)](https://github.com/IMIO/gha/blob/main/CHANGELOG.md)

This repository hosts a set of github actions we use to deploy our apps.

## Actions
- [iMio github actions](#imio-github-actions)
  - [Actions](#actions)
    - [build-push-notify](#build-push-notify)
      - [Inputs](#inputs)
      - [Example of usage](#example-of-usage)
    - [check-url-availibility](#check-url-availibility)
      - [Example of usage](#example-of-usage-1)
    - [code-analysis-notify](#code-analysis-notify)
      - [Inputs](#inputs-1)
      - [Example of usage](#example-of-usage-2)
    - [deb-build-push-notify](#deb-build-push-notify)
      - [Inputs](#inputs-2)
      - [Example of usage](#example-of-usage-3)
    - [helm-release-notify](#helm-release-notify)
      - [Inputs](#inputs-3)
      - [Example of usage](#example-of-usage-4)
    - [helm-test-notify](#helm-test-notify)
      - [Inputs](#inputs-4)
      - [Example of usage](#example-of-usage-5)
    - [mattermost-notify](#mattermost-notify)
      - [Inputs](#inputs-5)
      - [Example of usage](#example-of-usage-6)
    - [plone-package-test-notify](#plone-package-test-notify)
      - [Inputs](#inputs-6)
      - [Example of usage](#example-of-usage-7)
    - [plone-theme-build-push-notify](#plone-theme-build-push-notify)
      - [Inputs](#inputs-7)
      - [Example of usage](#example-of-usage-8)
    - [rundeck-notify](#rundeck-notify)
      - [Inputs](#inputs-8)
      - [Example of usage](#example-of-usage-9)
    - [tag-notify](#tag-notify)
      - [Inputs](#inputs-9)
      - [Example of usage](#example-of-usage-10)
    - [k8s-update-tag](#k8s-update-tag)
      - [Inputs](#inputs-10)
      - [Example of usage](#example-of-usage-11)
    - [trivy-scan-notify](#trivy-scan-notify)
      - [Inputs](#inputs-11)
      - [Example of usage](#example-of-usage-12)
    - [trivy-sbom-notify](#trivy-sbom-notify)
      - [Inputs](#inputs-12)
      - [Example of usage](#example-of-usage-13)
    - [claude-agent](#claude-agent)
      - [Inputs](#inputs-13)
      - [Example of usage](#example-of-usage-14)
  - [Contribute](#contribute)
    - [Release](#release)

### build-push-notify

build/push a docker image using docker/build-push-action and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| IMAGE_NAME             |    yes   | string |                 | Name of the image to build |
| IMAGE_TAGS             |    yes   | string |                 | Tags of the image to build and push (one per line)|
| REGISTRY_URL           |    yes   | string |                 | URL of the registry |
| REGISTRY_USERNAME      |    yes   | string |                 | Username to login to registry |
| REGISTRY_PASSWORD      |    yes   | string |                 | Password to login to registry |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |
| PLATFORMS              |    yes   | string | `"linux/amd64"` | Platforms to build the image for |
| CONTEXT                |    yes   | string | `"./"`          | Build context |
| DOCKERFILE             |    yes   | string | `"Dockerfile"`  | Name of the Dockerfile |
| BUILD_ARGS             |    yes   | string | `""`            | Build arguments to pass to the Dockerfile |
| TARGET                 |    no    | string |                 | Target stage to build |
| PRE_BUILD_COMMANDS     |    no    | string |                 | Optional commands to run before the build (one per line) |

#### Example of usage

[IMIO/docker-teleservices](https://github.com/IMIO/docker-teleservices/blob/7ee9bd77714bbbd1049c510aae222105460d72c6/.github/workflows/publish.yml#L16)

---
### check-url-availibility

Loop until a given url returns a 200 status-code. Can be used during deployments to test if an app is available.

| name                   | required |  type   | default         | description |
| ---------------------- | -------- | ------- | --------------- | ----------- |
|         URL            |   yes    |  string |                 | URL to test |
|       TIMEOUT          |   yes    | integer |       5         | Timeout (in minutes) |

#### Example of usage

[IMIO/docker-teleservices](https://github.com/IMIO/docker-teleservices/blob/7ee9bd77714bbbd1049c510aae222105460d72c6/.github/workflows/publish.yml#L59)

---
### code-analysis-notify

Run checks for Plone backend code and optionally notify via a mattermost webhook

This github action uses the [code-analysis-action](https://github.com/plone/code-analysis-action/tree/main) from the Plone organization.

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| BASE_DIR               |    no    | string |                 | Base directory |
| CHECK                  |    no    | string |                 | Checks to be used |
| PATH                   |    no    | string |                 | Path to be checked |
| LOG_LEVEL              |    no    | string | "INFO"          | Log level |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

[IMIO/imio.smartweb.core](https://github.com/IMIO/imio.smartweb.core/blob/fdb331eb004eed0744f419264f063a336b40d069/.github/workflows/plone-package-test-gha.yml#L16)

---
### deb-build-push-notify

Build a deb package, push it on a repository and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| REPOSITORY_URL         |   yes    | string |                 | URL of the repository |
| REPOSITORY_LOGIN       |   yes    | string |                 | Login for the repository |
| REPOSITORY_PASSWORD    |   yes    | string |                 | Passsword for the repository |
| PACKAGE_NAME           |   yes    | string |                 | Name of the package to build |
| PACKAGE_INSTALL_PATH   |   yes    | string | `'/usr/...'`    | Path to install package |
| PACKAGE_VERSION        |   yes    | string |                 | Package version |
| PACKAGE_DEPENDENCY     |   yes    | string | `'passerelle'`  | Package dependency |
| SIGNER_KEY             |   yes    | string |                 | Key to sign deb package (base64 encoded) |
| SIGNER_KEY_ID          |   yes    | string | `'9D4...'`      | ID of the key to sign deb package |
| SIGNER_KEY_PASSPHRASE  |   yes    | string |                 | Passphrase to sign deb package |
| MATTERMOST_WEBHOOK_URL |   no     | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

[IMIO/scripts-teleservices](https://github.com/IMIO/scripts-teleservices/blob/613d1563be3ddbafb3c66347022558c5dffb678c/.github/workflows/deb.yml#L20)

---
### helm-release-notify

Release a helm chart and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| HELM_VERSION           |    yes   | string | "3.12.3"       | Helm version to use |
| HELM_DEPENDENCIES      |    no    | string |                 | Helm dependencies |
| INDEX_DIR              |    yes   | string | "."             | Index directory |
| CHARTS_DIR             |    yes   | string | "."             | Charts directory |
| TARGET_DIR             |    yes   | string | "test"          | Target directory to release |
| APP_ID                 |    yes   | string |                 | Github App ID |
| PRIVATE_KEY            |    yes   | string |                 | Github App private key |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

/

---
### helm-test-notify

Lint and test a helm chart and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| PYTHON_VERSION         |    yes   | string | "3.10"          | Python version to use |
| HELM_VERSION           |    yes   | string | "v3.12.3"       | Helm version to use |
| HELM_RELEASE           |    yes   | string | "test"          | Helm release name |
| HELM_NAMESPACE         |    yes   | string | "test"          | Helm namespace name |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

/

---
### mattermost-notify

Send a rich color-coded notification to a Mattermost webhook.

Notifications use Mattermost attachments with a green strip on success and red on failure, an emoji prefix, a structured bold-field body, and an auto-appended link to the GitHub Actions run. If `MATTERMOST_WEBHOOK_URL` is omitted the step is silently skipped.

#### Inputs

| name                   | required | type   | default | description |
| ---------------------- | -------- | ------ | ------- | ----------- |
| MATTERMOST_WEBHOOK_URL |    no    | string | `""`    | Webhook URL. If empty, notification is skipped. |
| TITLE                  |    yes   | string |         | Short notification title (e.g. `"Docker Build & Push"`) |
| BODY                   |    no    | string | `""`    | Notification body (Markdown, newlines supported). A link to the GitHub Actions run is always appended automatically. |
| STATUS                 |    yes   | string |         | Job outcome: `success` or `failure` |

#### Example of usage

```yaml
- name: Notify on Mattermost
  if: always()
  uses: imio/gha/mattermost-notify@v7
  with:
    MATTERMOST_WEBHOOK_URL: ${{ secrets.MATTERMOST_WEBHOOK_URL }}
    STATUS: ${{ steps.build.outcome == 'success' && 'success' || 'failure' }}
    TITLE: "My Job"
    BODY: |
      **Branch:** ${{ github.ref_name }}
      **Commit:** ${{ github.sha }}
```

---
### plone-package-test-notify

Test a Plone package and optionally notify via a mattermost webhook

> [!WARNING] 
> Python 2 support has been dropped in v5. If you still need it, use [v4](https://github.com/IMIO/gha/tree/v4)

#### Inputs

| name                          | required | type   | default            | description |
| ----------------------------- | -------- | ------ | ------------------ | ----------- |
| BUILDOUT_COMMAND              |    yes   | string | "buildout"         | Command to run buildout |
| BUILDOUT_CONFIG_FILE          |    yes   | string | "buildout.cfg"     | Buildout config file |
| BUILDOUT_OPTIONS              |    no    | string |                    | Options to pass to buildout |
| CACHE_KEY                     |    no    | string |                    | key to use in actions/cache |
| INSTALL_DEPENDENCIES_COMMANDS |    no    | string |                    | Install dependencies commands (one per line) |
| MATTERMOST_WEBHOOK_URL        |    no    | string |                    | Webhook URL to send notifications on Mattermost |
| PYTHON_VERSION                |    yes   | string | "3.13"             | Python version to use |
| TEST_COMMAND                  |    yes   | string | "bin/test"         | Test command to run |
| UV_VERSION                    |    yes   | string | "0.7.13"           | uv version to use |

#### Example of usage

[IMIO/imio.smartweb.core](https://github.com/IMIO/imio.smartweb.core/blob/fdb331eb004eed0744f419264f063a336b40d069/.github/workflows/plone-package-test-gha.yml#L33)

---
### plone-theme-build-push-notify

Build a theme, upload it to a plone site and optionally notify on Mattermost

#### Inputs

| name                   | required | type   | default      | description |
| ---------------------- | -------- | ------ | -------------| ----------- |
| THEME_PATH             |    yes   | string |              | Folder where theme files are located |
| PLONE_URL              |    yes   | string |              | URL of the Plone site |
| PLONE_USERNAME         |    yes   | string |              | Username to login to Plone |
| PLONE_PASSWORD         |    yes   | string |              | Password to login to Plone |
| MATTERMOST_WEBHOOK_URL |    no    | string |              | Webhook URL to send notifications on Mattermost |

#### Example of usage

[IMIO/imio_smartweb_themes](https://github.com/IMIO/imio_smartweb_themes/blob/2268e1ee7350214b7fe7e98c4353622a61c3250a/.github/workflows/build-upload.yml#L117)

---
### repository-dispatch-notify

Trigger a repository dispatch event and optionally notify on Mattermost

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| REPOSITORY             |    yes   | string |                 | Repository to trigger the dispatch event |
| GIT_REFERENCE          |    no    | string | "main"          | Reference to trigger the event on |
| INPUTS                 |    no    | string | "{}"            | Inputs to pass to the workflow, Exemple : {"input1":"abc", "input2":"abc"} |
| REPOSITORY_OWNER       |    yes   | string |                 | Repository owner |
| WORKFLOW_FILENAME      |    yes   | string |                 | Filename of the workflow to trigger |
| APP_ID                 |    yes   | string |                 | GitHub App ID |
| APP_PRIVATE_KEY        |    yes   | string |                 | GitHub App private key |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

/

---
### rundeck-notify

call a rundeck job and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| RUNDECK_URL            |    yes   | string |                 | URL of the Rundeck server |
| RUNDECK_TOKEN          |    yes   | string |                 | Auth token to call Rundeck job |
| RUNDECK_JOB_ID         |    yes   | string |                 | ID of the rundeck job to call |
| RUNDECK_PARAMETERS     |    no    | string |                 | Parameters to pass to the Rundeck job |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

[IMIO/buildout.news](https://github.com/IMIO/buildout.news/blob/6b229a3a0e00dda2986e496ebc7b70da2069273e/.github/workflows/prod.yml#L35)

---
### tag-notify

Add tags to a docker image and optionally notify via a mattermost webhook

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| IMAGE_NAME             |    yes   | string |                 | Name of the image to tag |
| IMAGE_TAG              |    yes   | string | `"staging"`     | Actual tag of the image |
| NEW_IMAGE_TAGS         |    yes   | string |                 | Tags to add to the image (one per line) |
| REGISTRY_URL           |    yes   | string |                 | URL of the registry |
| REGISTRY_USERNAME      |    yes   | string |                 | Username to login to registry |
| REGISTRY_PASSWORD      |    yes   | string |                 | Password to login to registry |
| MATTERMOST_WEBHOOK_URL |    no    | string |                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

[IMIO/buildout.ideabox](https://github.com/IMIO/buildout.ideabox/blob/9e8218d6f52a5060d14139864b6b0d993f633202/.github/workflows/prod.yml#L16)

---
### k8s-update-tag

Update a component tag in Kubernetes values file and commit to repository. This action is useful for automated deployments where you want to update the image tag in your Kubernetes configuration files.

#### Inputs

| name                   | required | type   | default         | description |
| ---------------------- | -------- | ------ | --------------- | ----------- |
| TAG                    |    yes   | string |                 | Tag to set for the component (e.g., commit SHA) |
| REPO_TOKEN_NAME        |    yes   | string |                 | Name of the repository access token |
| REPO_ACCESS_TOKEN      |    yes   | string |                 | Repository access token for authentication |
| REPO_URL               |    yes   | string |                 | Repository URL (without https://) |
| TARGET_BRANCH          |    no    | string | `"main"`        | Target branch to update |
| VALUES_FILE_PATH       |    yes   | string |                 | Path to the values file to update |

#### Example of usage

```yaml
- name: Update Kubernetes tag
  uses: IMIO/gha/k8s-update-tag@v5
  with:
    TAG: ${{ github.sha }}
    REPO_TOKEN_NAME: DEPLOY_TOKEN
    REPO_ACCESS_TOKEN: ${{ secrets.K8S_DEPLOY_TOKEN }}
    REPO_URL: github.com/myorg/k8s-configs.git
    TARGET_BRANCH: main
    VALUES_FILE_PATH: staging/myapp/values-dev.yaml
```

---
### trivy-scan-notify

Run a [Trivy](https://github.com/aquasecurity/trivy) scan (container image, filesystem or IaC config), upload the SARIF report to GitHub Code Scanning, archive it as a workflow artifact, and optionally notify via Mattermost with parsed severity counts.

External actions are pinned by SHA as required by the iMio security référentiel (§5.5 CI/CD).

> [!IMPORTANT]
> The calling workflow must grant `permissions: security-events: write` for the SARIF upload to Code Scanning to succeed. On **private** repositories, GitHub Advanced Security must be enabled.
>
> When `CLAUDE_ANALYSIS=true`, the workflow also needs `repository-advisories: write` to create private draft security advisories.

#### Inputs

| name                   | required | type    | default                   | description |
| ---------------------- | -------- | ------- | ------------------------- | ----------- |
| SCAN_TYPE              |   yes    | string  |                           | One of `image`, `fs`, `config` |
| IMAGE_REF              |   cond.  | string  |                           | Image reference to scan (required when `SCAN_TYPE=image`) |
| SCAN_REF               |   no     | string  | `"."`                     | Filesystem path (used when `SCAN_TYPE` is `fs` or `config`) |
| SEVERITY               |   no     | string  | `"HIGH,CRITICAL"`         | Comma-separated severity levels to report |
| SCANNERS               |   no     | string  | *(per-type default)*      | Trivy scanners. If empty: `image`→`vuln,secret,misconfig`, `fs`→`vuln,secret`, `config`→`secret,misconfig` |
| EXIT_CODE              |   no     | string  | `"1"`                     | Exit code when findings match `SEVERITY` (set to `"0"` during bootstrap) |
| IGNORE_UNFIXED         |   no     | string  | `"true"`                  | Ignore vulnerabilities without a known fix |
| TRIVYIGNORES           |   no     | string  | `".trivyignore"`          | Path to a `.trivyignore` file |
| UPLOAD_SARIF           |   no     | string  | `"true"`                  | Upload SARIF to GitHub Code Scanning |
| SARIF_CATEGORY         |   no     | string  | `"trivy-<SCAN_TYPE>"`     | Code Scanning category for split results |
| TRIVY_USERNAME         |   no     | string  |                           | Username for a private image registry |
| TRIVY_PASSWORD         |   no     | string  |                           | Password for a private image registry |
| GITHUB_TOKEN           |   no     | string  |                           | Pass `secrets.GITHUB_TOKEN` to avoid Trivy DB rate-limits and to allow Claude to create security advisories |
| MATTERMOST_WEBHOOK_URL |   no     | string  |                           | Webhook URL to send notifications on Mattermost |
| CLAUDE_ANALYSIS        |   no     | string  | `"false"`                 | Set to `"true"` to invoke Claude to analyze findings and create private draft security advisories (requires `ANTHROPIC_API_KEY`) |
| ANTHROPIC_API_KEY      |   no     | string  |                           | Anthropic API key, required when `CLAUDE_ANALYSIS=true`. Pass `secrets.ANTHROPIC_API_KEY`. |
| CLAUDE_SEVERITIES      |   no     | string  | `"CRITICAL,HIGH"`         | Comma-separated severities Claude should create advisories for. Append `,MEDIUM` to include medium findings. |

#### Outputs

| name     | description |
| -------- | ----------- |
| critical | Number of CRITICAL findings |
| high     | Number of HIGH findings |
| medium   | Number of MEDIUM findings |

#### Example of usage

```yaml
name: Trivy

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read
  security-events: write  # required to upload SARIF

jobs:
  trivy-fs:
    runs-on: ubuntu-latest
    steps:
      - uses: imio/gha/trivy-scan-notify@v7
        with:
          SCAN_TYPE: fs
          SCAN_REF: .
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          MATTERMOST_WEBHOOK_URL: ${{ secrets.MATTERMOST_WEBHOOK_URL }}

  trivy-iac:
    runs-on: ubuntu-latest
    steps:
      - uses: imio/gha/trivy-scan-notify@v7
        with:
          SCAN_TYPE: config
          SCAN_REF: .
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          MATTERMOST_WEBHOOK_URL: ${{ secrets.MATTERMOST_WEBHOOK_URL }}

  trivy-image:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd  # v6.0.2
      - run: docker build -t ${{ github.repository }}:${{ github.sha }} .
      - uses: imio/gha/trivy-scan-notify@v7
        with:
          SCAN_TYPE: image
          IMAGE_REF: ${{ github.repository }}:${{ github.sha }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          MATTERMOST_WEBHOOK_URL: ${{ secrets.MATTERMOST_WEBHOOK_URL }}
```

#### Two-job pattern with manual approval

Use this pattern to gate Claude analysis behind a human approval step. Job 1 scans and notifies; reviewers see the finding counts in Mattermost and approve job 2 only when Claude analysis is worth running. The prompt stays versioned inside the action — nothing is duplicated across repositories.

> [!NOTE]
> Create a `security-review` environment in repo Settings → Environments and add required reviewers before using this pattern.

```yaml
jobs:
  scan:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
    outputs:
      critical: ${{ steps.trivy.outputs.critical }}
      high: ${{ steps.trivy.outputs.high }}
    steps:
      - uses: imio/gha/trivy-scan-notify@v7
        id: trivy
        with:
          SCAN_TYPE: image
          IMAGE_REF: registry.example.org/myapp:${{ github.sha }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          MATTERMOST_WEBHOOK_URL: ${{ secrets.MATTERMOST_WEBHOOK_URL }}

  claude-analysis:
    needs: scan
    if: needs.scan.outputs.critical > 0 || needs.scan.outputs.high > 0
    environment: security-review   # pauses for human approval
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
      repository-advisories: write
    steps:
      - uses: imio/gha/trivy-scan-notify@v7
        with:
          SCAN_TYPE: image
          IMAGE_REF: registry.example.org/myapp:${{ github.sha }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          CLAUDE_ANALYSIS: 'true'
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          EXIT_CODE: '0'         # findings already flagged in job 1
          UPLOAD_SARIF: 'false'  # already uploaded in job 1
```

---
### trivy-sbom-notify

Generate a CycloneDX (or SPDX) SBOM for a container image with Trivy, upload it as a workflow artifact, and optionally notify on Mattermost. This action does not block the pipeline.

#### Inputs

| name                   | required | type    | default                         | description |
| ---------------------- | -------- | ------- | ------------------------------- | ----------- |
| IMAGE_REF              |   yes    | string  |                                 | Full registry-qualified image reference |
| FORMAT                 |   no     | string  | `"cyclonedx"`                   | `cyclonedx` or `spdx-json` |
| OUTPUT                 |   no     | string  | `"sbom.cdx.json"`               | Output file path |
| ARTIFACT_NAME          |   no     | string  | `"sbom-${{ github.sha }}"`      | Name of the workflow artifact |
| RETENTION_DAYS         |   no     | string  | `"90"`                          | Artifact retention in days |
| TRIVY_USERNAME         |   no     | string  |                                 | Username for a private image registry |
| TRIVY_PASSWORD         |   no     | string  |                                 | Password for a private image registry |
| GITHUB_TOKEN           |   no     | string  |                                 | Pass `secrets.GITHUB_TOKEN` to avoid rate-limits |
| MATTERMOST_WEBHOOK_URL |   no     | string  |                                 | Webhook URL to send notifications on Mattermost |

#### Example of usage

```yaml
jobs:
  sbom:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    needs: trivy-image
    steps:
      - uses: imio/gha/trivy-sbom-notify@v7
        with:
          IMAGE_REF: registry.example.org/${{ github.repository }}:${{ github.sha }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          MATTERMOST_WEBHOOK_URL: ${{ secrets.MATTERMOST_WEBHOOK_URL }}
```

---
### claude-agent

Run a [Claude Code](https://docs.anthropic.com/claude/claude-code) agent with a given prompt in a CI pipeline. Thin, opinionated wrapper around `anthropics/claude-code-action` with prompt composition, optional file exposure, model selection, and GitHub API access for operations such as creating security advisories.

> [!NOTE]
> The calling workflow must grant the permissions required for the operations Claude will perform. For security advisory creation, add `repository-advisories: write`.

#### Inputs

| name              | required | type   | default               | description |
| ----------------- | -------- | ------ | --------------------- | ----------- |
| PROMPT            |   yes    | string |                       | Instructions for Claude |
| FILES             |   no     | string |                       | Newline-separated list of file paths to expose to Claude (appended to the prompt as a "Files to examine" section) |
| ANTHROPIC_API_KEY |   yes    | string |                       | Anthropic API key. Pass `secrets.ANTHROPIC_API_KEY`. |
| MODEL             |   no     | string | `"claude-sonnet-4-6"` | Claude model ID |
| GITHUB_TOKEN      |   no     | string |                       | GitHub token forwarded to Claude for GitHub API operations (e.g. creating security advisories). Pass `secrets.GITHUB_TOKEN`. |

Claude's output is displayed in the GitHub Actions Step Summary (`display_report: true`).

#### Example of usage

```yaml
jobs:
  security-advisory:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      repository-advisories: write
    steps:
      - uses: imio/gha/claude-agent@v7
        with:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PROMPT: |
            Review the dependency list and create a private draft security advisory
            for any known critical vulnerability you find.
          FILES: |
            package.json
            requirements.txt
```

Combined with `trivy-scan-notify` (opt-in via `CLAUDE_ANALYSIS`):

```yaml
permissions:
  contents: read
  security-events: write
  repository-advisories: write

steps:
  - uses: imio/gha/trivy-scan-notify@v7
    with:
      SCAN_TYPE: image
      IMAGE_REF: registry.example.org/myapp:${{ github.sha }}
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      MATTERMOST_WEBHOOK_URL: ${{ secrets.MATTERMOST_WEBHOOK_URL }}
      CLAUDE_ANALYSIS: 'true'
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      CLAUDE_SEVERITIES: 'CRITICAL,HIGH,MEDIUM'
```

## Contribute

### Release

A new release is issued when a tag beginning with v is pushed.
The main release (for instance v3) will also be updated with the latest tag.

The release note is automatically populated using the "[tag]" section from the CHANGELOG.md .

[See the CHANGELOG.md file for an example](https://github.com/IMIO/gha/blob/66f298e6e5081e5e917df21e1036c6fa52246a8d/CHANGELOG.md?plain=1#L3)

Typically, you will first update the changelog ([Example commit](https://github.com/IMIO/gha/commit/edb3c35ac9eac8b489d1a41972ee74f930859d31)).

Then, you will push the tags.


```bash
git add CHANGELOG.md
git commit -m 'doc: Release v5.0.0'
git tag -a -m 'release v5.0.0' v5.0.0
git push --follow-tags
```
