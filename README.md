# Project Title

Project description

## Installation

### Requirements

- [UV](https://docs.astral.sh/uv/)
- Rename the project in [pyproject.toml](pyproject.toml) file

### Sync Dependencies

```bash
  uv sync
```

## Running the project

To run the project locally, run the following command:

```bash
  uv run python -m src.python_template
```

## Running Tests

To run tests, run the following command:

```bash
  uv run pytest
```

## Linting and formatting

We can use UV tools to lint and format the code.

```bash
  uvx ruff check . --fix
  uvx ruff format .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
