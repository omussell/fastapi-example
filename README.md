# Example FastAPI Application

move most of this doc into the mkdocs docs. Keep this file basic.

This repo is supposed to be an example FastAPI application with the bare minimum to get an API up and running with FastAPI, SQLAlchemy, Alembic and SQLite. Its purpose is therefore mainly for rapid prototyping and not for production applications.

For a more complete example using backend, frontend, celery, postgres, docker etc., see this repo: [Full Stack FastAPI PostgreSQL](https://github.com/tiangolo/full-stack-fastapi-postgresql)

For a real world application, see [Netflix Dispatch](https://github.com/Netflix/dispatch)


## Single file app

uvicorn main:app

## Multiple files app

uvicorn app.main:app


# API Performance Test

[](https://github.com/nginxinc/rtapi)

`~/go/bin/rtapi -f rtapi.yaml -o output.pdf`


# SQLAlchemy models vs Pydantic models

Its a bit confusing when you first look at setting up FastAPI to use a database because it looks like you are duplicating a model with both pydantic and sqlalchemy. The reason for this is because FastAPI can function without a database, and without pydantic too. Pydantic models give you documentation, serialisation and validation. SQLAlchemy models are for interacting with the database.

While they solve different problems, you can end up with duplicate looking classes doing effectively the same thing. However, the separation is that pydantic is purely for the web app validation, and sqlalchemy is purely for the SQL validation.

This difference is bridged by [Pydantic's ORM_mode](https://pydantic-docs.helpmanual.io/usage/models/#orm-mode-aka-arbitrary-class-instances). When orm_mode is set to true on a pydantic model, pydantic understands the data returned by a sqlalchemy model. You can then declare the pydantic model in the `response_model` argument in your path operations. Then you will be able to return a database model and it will read data from it.

# Build documentation

There is a fabric script included for building the documentation. This is built using mkdocs and the mkautodoc extension. This means documentation can be created for both the user manual and the API via docstrings.

```shell
# Build docs
fab build

# Live-reload server
fab serve
```

For mkautodoc to work you need to set the `PYTHONPATH` variable to the git root path. This is already done in the fabfile.

# Development Tools

## Code Complexity
- [lizard](https://pypi.org/project/lizard/)
- [radon](https://pypi.org/project/radon/)

### Lizard
`lizard -x'*/tests/*' -l python -w app`

### Radon
```
radon cc --min B --average --total-average app
radon mi --min B app
```


## Documentation
- [mkdocs](https://www.mkdocs.org/)
- [mkautodoc](https://github.com/tomchristie/mkautodoc)

### Mkdocs

```
cd ../
mkdocs new fastapi-example
cd fastapi-example
```


## Development Tools
- [ipython](https://ipython.readthedocs.io/en/stable/)
- [ipdb](https://pypi.org/project/ipdb/)
- [pre-commit](https://pre-commit.com/)

### Pre-Commit

`pre-commit install` to add the hooks to the repo


## Formatting/Styling
- [black](https://black.readthedocs.io/en/stable/)
- [isort](https://pypi.org/project/isort/)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [flake8-blind-except](https://pypi.org/project/flake8-blind-except/)
- [flake8-bugbear](https://pypi.org/project/flake8-bugbear/)
- [flake8-coding](https://pypi.org/project/flake8-coding/)
- [flake8-commas](https://pypi.org/project/flake8-commas/)
- [flake8-debugger](https://pypi.org/project/flake8-debugger/)
- [flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
- [flake8-isort](https://pypi.org/project/flake8-isort/)
- [flake8-quotes](https://pypi.org/project/flake8-quotes/)
- [flake8-sfs](https://pypi.org/project/flake8-sfs/)
- [pydocstyle](https://pypi.org/project/pydocstyle/)

### Black

`black app`

Configuration options are set in `pyproject.toml`.

### Isort

`isort app/*.py`

### Flake8

`flake8 app`

The following plugins are used:

- flake8-blind-except - Checks for blind/catch-all `except:` statements
- flake8-bugbear - Find common bugs and design problems
- flake8-coding - Ensure file contains magic `coding` comment
- flake8-commas - Checks commas exist in different places
- flake8-debugger - Checks for pdb/ipdb imports and set traces
- flake8-docstrings - Runs `pydocstyle` to check docstrings format
- flake8-isort - Check if the imports are sorted in the way you expect
- flake8-quotes - Check that a specific quote type is used. Prefer double.
- flake8-sfs - Check string format. Prefer f-strings.

### Pydocstyle

`pydocstyle app`

## Security
- [bandit](https://pypi.org/project/bandit/)

### Bandit

`bandit -r app`

To exclude directories from checks, add a `.bandit` file:

```
[bandit]
exclude: tests
```

## Type Hints
- [mypy](https://mypy.readthedocs.io/en/latest/)

### Mypy

`mypy app`
