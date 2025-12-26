# Python App Template

This project provide a template for Python projects, including a basic structure and configuration files to help you get started quickly.
It aims to enforce best practices and provide a consistent development experience.

## Installation

### Requirements

- [UV](https://docs.astral.sh/uv/) package manager

### Clone the repository

```bash
  git clone https://github.com/PierreLapolla/python_template.git
  cd python_template
```

### Initialize your environment

```bash
  uv sync
```

## Running the project

To run the project locally, run the following command:

```bash
  uv run -m src.app
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

## License

This project is licensed under the MIT [LICENSE](LICENSE)
