# Project
from fabric import task

git_root = "/home/oem/fastapi-example"
# path_override = f"{git_root}/venv/bin:/home/oem/.local/bin:/home/oem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"


@task
def build(c):
    with c.cd(git_root):
        c.run(
            f"mkdocs build",
            env={"PATH": f"{git_root}/venv/bin", "PYTHONPATH": "/home/oem/fastapi-example"},
        )


@task()
def serve(c):
    with c.cd(git_root):
        c.run(
            "mkdocs serve",
            env={"PATH": f"{git_root}/venv/bin", "PYTHONPATH": "/home/oem/fastapi-example"},
        )
