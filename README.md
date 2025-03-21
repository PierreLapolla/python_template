# Project Title
## Installation

### Requirements

- [UV](https://docs.astral.sh/uv/)

### Sync Dependencies

```bash
  uv sync
```

If you don't want to use uv, dependencies are listed in the [pyproject.toml](pyproject.toml) file.

## Run Locally

To run the project locally, run the following command:

```bash
  uv run python -m src.python_template
```

## Running Tests

To run tests, run the following command:

```bash
  uv run pytest --cov=. --cov-report=html
```

## Linting and formatting

We can use UV tools to lint and format the code.

```bash
  uvx ruff check . --fix
  uvx ruff format .
```

## License

No license has been defined for this project yet.