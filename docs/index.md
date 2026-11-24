# Python App Template

A small, opinionated starting point for modern Python applications. It includes
packaging, tests, linting, type information, Docker support, pre-commit hooks,
and a documentation site deployed with GitHub Pages.

## Get started

You need Python 3.10 or newer and the
[uv package manager](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/PierreLapolla/python_template.git
cd python_template
uv sync
uv run pre-commit install
```

Run the example application:

```bash
uv run app
```

The command writes `Hello from python-template!` through the configured logger.

## What is included

- A `src` package layout with typed-package support
- Dependency and environment management with uv
- Tests and coverage with pytest
- Linting and formatting with Ruff
- Git hooks with pre-commit
- GitHub Actions CI running hooks and tests, and enforcing a version bump
- Tag-driven releases publishing the Docker image to GitHub Container Registry
- A multi-stage, non-root Docker image
- Documentation built by Zensical and deployed by GitHub Actions

See [Development](development.md) for common commands and instructions for
adapting the template.
