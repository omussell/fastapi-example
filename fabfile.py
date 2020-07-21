# Project
from fabric import task

git_root = "/home/oem/fastapi-example"
local_env = {
    "PATH": f"{git_root}/venv/bin",
    "PYTHONPATH": f"{git_root}/app",
}

@task
def format(c):
    with c.cd(git_root):
        c.run(
            "black app", env=local_env,
        )
        c.run(
            "isort app -rc", env=local_env,
        )

@task
def lint(c):
    with c.cd(git_root):
        c.run(
            "black app --check", env=local_env,
        )
        c.run(
            "isort app --check-only", env=local_env,
        )


@task
def build_docs(c):
    with c.cd(git_root):
        c.run(
            f"mkdocs build", env=local_env,
        )


@task()
def serve_docs(c):
    with c.cd(git_root):
        c.run(
            "mkdocs serve", env=local_env,
        )


@task()
def run(c):
    with c.cd(f"{git_root}/app"):
        c.run(
            "uvicorn main:app --reload", env=local_env,
        )


@task()
def makemigrations(c, message):
    with c.cd(f"{git_root}/app"):
        c.run(
            f'alembic revision --autogenerate -m "{message}"', env=local_env,
        )


@task()
def migrate(c):
    with c.cd(f"{git_root}/app"):
        c.run(
            f"alembic upgrade head", env=local_env,
        )
