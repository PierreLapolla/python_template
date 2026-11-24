![Ruff](https://img.shields.io/badge/ruff-enabled-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

# Python App Template

This project provides a starter structure and tooling for Python apps, aiming for a consistent and modern dev experience.

Read the full [project documentation](https://pierrelapolla.github.io/python_template/).

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
  uv run app
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

## Versioning

CI fails unless the version in `pyproject.toml` is higher than on the target
branch. Bump it in every pull request (or push to `main`/`master`):

```bash
  uv version --bump patch  # or minor / major
```

## Documentation

Preview the documentation locally:

```bash
  uv run zensical serve
```

The [documentation site](https://pierrelapolla.github.io/python_template/) is
automatically deployed to GitHub Pages when changes are pushed to `main` or
`master`.

## License

This project is licensed under the MIT [LICENSE](LICENSE)
