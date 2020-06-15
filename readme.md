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
