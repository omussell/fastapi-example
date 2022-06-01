#! /bin/sh

rm /home/oem/hortus/db.sqlite3
alembic revision --autogenerate -m "Initial"
alembic upgrade head
