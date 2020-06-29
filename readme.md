# Example FastAPI Application

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
