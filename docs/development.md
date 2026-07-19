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

## Build and run the container

```bash
docker build -t python-template .
docker run --rm python-template
```

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
