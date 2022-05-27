# FastAPI-Example

An example application using FastAPI, Pydantic, encode/orm, encode/databases and encode/uvicorn.

Project layout is inspired by [the FastAPI docs](https://fastapi.tiangolo.com/tutorial/bigger-applications/) and [Dispatch](https://github.com/Netflix/dispatch/tree/develop/src/dispatch).

# Features

- FastAPI, Pydantic Models, SQLModel and Async SQL all tied together
- DB migrations using Alembic
- Settings via Pydantic / Dotenv
- Development tools - black, ipython, isort etc.
- Documentation for users and developers with mkdocs and mkdocstrings
- Scripts via Fabric for formatting, linting, building docs, publishing new versions etc.
- SQLite by default but can be changed to any database that SQLAlchemy supports.

# Installation

```
git clone git@github.com:omussell/fastapi-example.git

# Create the initial migrations
fab makemigrations

# Run the migrations to create the SQLite DB
fab migrate
```

# Usage

From the git root:

Development examples:
::: fabfile

# Documentation

[Link](https://omussell.github.io/fastapi-example)
