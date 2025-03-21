# Project Title
## Installation

### Requirements

- [UV](https://docs.astral.sh/uv/)

### Sync Dependencies

```bash
  uv sync
```

## Run Locally

To run the project locally, run the following command:

```bash
  uv run python -m src.python_template
```

## Running Tests

To run tests, run the following command:

```bash
  uv run pytest -c pytest.ini --cov=. --cov-report=html
```

## Linting and formatting

We can use UV tools to lint and format the code.

```bash
  uvx ruff check . --fix
  uvx ruff format .
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
