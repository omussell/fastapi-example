# Example FastAPI Application

# Documentation

[Link](https://omussell.github.io/fastapi-example)

This repo is supposed to be an example FastAPI application with the bare minimum to get an API up and running with FastAPI, SQLModel, Alembic and SQLite. Its purpose is therefore mainly for rapid prototyping and simple production applications.

For a more complete example using backend, frontend, celery, postgres, docker etc., see this repo: [Full Stack FastAPI PostgreSQL](https://github.com/tiangolo/full-stack-fastapi-postgresql)

For a real world application, see [Netflix Dispatch](https://github.com/Netflix/dispatch)


## Single file app

uvicorn main:app

## Multiple files app

uvicorn app.main:app

# Build documentation

# Development Tools

## Documentation
- [mkdocs](https://www.mkdocs.org/)

### Mkdocs



## Development Tools
- [ipython](https://ipython.readthedocs.io/en/stable/)


## Formatting/Styling
- [black](https://black.readthedocs.io/en/stable/)
- [isort](https://pypi.org/project/isort/)

### Black

`black app`

### Isort

`isort app`

## Type Hints
- [mypy](https://mypy.readthedocs.io/en/latest/)

### Mypy

`mypy app`
