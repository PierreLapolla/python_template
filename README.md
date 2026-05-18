![Ruff](https://img.shields.io/badge/ruff-enabled-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

# Python App Template

This project provides a starter structure and tooling for Python apps, aiming for a consistent and modern dev experience.

## Installation

### Requirements

- [UV](https://docs.astral.sh/uv/) package manager, see [Installing uv](https://docs.astral.sh/uv/getting-started/installation/)

### Clone the repository

```bash
  git clone https://github.com/PierreLapolla/python_template.git
  cd python_template
```

### Initialize your environment

```bash
  uv sync
  uv run pre-commit install
```

## Running the project

To run the project locally, run the following command:

```bash
  uv run -m src.app
```

## Docker

Build the image:

```bash
  docker build -t python-template .
```

Run the container:

```bash
  docker run --rm python-template
```

## Tests, linting and formatting

```bash
  uv run pytest
```

```bash
  uvx ruff check . --fix
```

```bash
  uvx ruff format .
```

Run all hooks manually:

```bash
  uv run pre-commit run --all-files
```

## GitHub Actions CI/CD

Project includes GitHub Actions workflow at [.github/workflows/pypi-cicd.yml](.github/workflows/pypi-cicd.yml).

What workflow does:

- Runs tests on pushes, pull requests, manual runs
- Tests against Python `3.13` and `3.14`
- Builds package with `uv build`
- Publishes to PyPI when you push tag matching `v*` like `v0.1.0`
- Uses `uv` for dependency sync, test execution, build, publish

## PyPI token setup

1. Create PyPI API token on [PyPI account settings](https://pypi.org/manage/account/token/).
2. In GitHub repo, open `Settings` -> `Secrets and variables` -> `Actions`.
3. Add new repository secret named `PYPI_TOKEN`.
4. Paste PyPI token value as secret content.

Recommend using project-scoped token for least privilege.

## Release flow

After `PYPI_TOKEN` secret exists:

```bash
git tag v0.1.0
git push origin v0.1.0
```

That tag triggers workflow to:

- run test matrix
- build distribution
- publish `dist/*` to PyPI

If you want TestPyPI first, duplicate workflow publish job and switch `uv publish` target to TestPyPI credentials.

## License

This project is licensed under the MIT [LICENSE](LICENSE)
