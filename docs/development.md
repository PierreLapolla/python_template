# Development

## Install the development environment

```bash
uv sync
uv run pre-commit install
```

The application package lives in `src/app`, and its tests live in
`tests/test_app`.

## Run quality checks

Run the test suite with coverage:

```bash
uv run pytest
```

Check and format the code:

```bash
uvx ruff check . --fix
uvx ruff format .
```

Run every configured pre-commit hook:

```bash
uv run pre-commit run --all-files
```

## Bump the version

`scripts/check_version_bump.py` fails unless the committed version in
`pyproject.toml` is strictly higher than on a base ref. It runs:

- as a **pre-push** hook, comparing against the merge-base with `origin`'s
  default branch, so the push is blocked locally;
- in the `version` job of `.github/workflows/ci.yml`, comparing against the
  pull request base or the previous commit, as a backstop for
  `git push --no-verify`.

`uv run pre-commit install` installs both the pre-commit and pre-push hooks.
Clones set up before this hook existed must run it again. Bump at least the
patch version once per branch:

```bash
uv version --bump patch  # 0.1.0 -> 0.1.1
uv version --bump minor  # 0.1.1 -> 0.2.0
uv version --bump major  # 0.2.0 -> 1.0.0
```

`uv version` updates both `pyproject.toml` and `uv.lock`.

## Build and run the container

```bash
docker build -t python-template .
docker run --rm python-template
```

## Release a new version

Releases are driven by git tags and handled by `.github/workflows/cd.yml`:

1. Bump the version in your branch with `uv version --bump patch` (or `minor`,
   `major`) and merge it into `master`.
2. Tag the merged commit and push the tag:

    ```bash
    git switch master && git pull
    git tag "v$(uv version --short)"
    git push origin "v$(uv version --short)"
    ```

3. The workflow checks that the tag matches `pyproject.toml`, builds the image
   for `linux/amd64` and `linux/arm64`, pushes it to
   `ghcr.io/<owner>/<repo>` tagged `X.Y.Z`, `X.Y` and `latest`, and creates a
   GitHub release with generated notes.

Pull requests that change the `Dockerfile`, the source code or the dependencies
also build the image and run it once as a smoke test, without publishing it.

No secrets are required: the workflow uses the built-in `GITHUB_TOKEN`. If the
published package is private, change its visibility in the package settings
on GitHub.

## Work on the documentation

Start the Zensical development server:

```bash
uv run zensical serve
```

Build the static site locally:

```bash
uv run zensical build --clean
```

Changes pushed to `main` or `master` are deployed to GitHub Pages by
`.github/workflows/docs.yml`. GitHub Pages must use **GitHub Actions** as its
source in the repository settings.

## Adapt the template

Before starting a new project, update the package name, description, author,
repository URLs, and console script in `pyproject.toml`. Rename `src/app` and
adjust the test imports if the Python package name changes. Update
`zensical.toml` with the new documentation title, author, repository, and
canonical URL.
