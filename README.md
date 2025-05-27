# Python Template

This project provide a template for Python projects, including a basic structure and configuration files to help you get started quickly.
It aims to enforce best practices and provide a consistent development experience.

## Installation

### Requirements

- [UV](https://docs.astral.sh/uv/)
- Project name in [pyproject.toml](pyproject.toml) file must be the same as your module's name in `src` folder.

### Clone the repository

```bash
  git clone https://github.com/PierreLapolla/python_template.git
  cd python_template
```

### Initialize the project:

```bash
  uv sync
```

## Running the project

To run the project locally, run the following command:

```bash
  uv run python -m src.python_template
```

## Tests, linting and formatting - AUTOMATED

These steps are automatically handled by [pre-commit](https://pre-commit.com/) hooks defined
in [.pre-commit-config.yaml](.pre-commit-config.yaml).
Additionally, you can run them manually with the following commands:

```bash
  uv run pytest
```

```bash
  uvx ruff check . --fix
```

```bash
  uvx ruff format .
```

You can also run pre-commit hooks manually with:

```bash
  uv run pre-commit run --all-files
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
