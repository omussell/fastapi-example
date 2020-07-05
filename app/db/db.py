# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
## SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
#
# engine = create_engine(
#    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
# import models

# Import all the models, so that Base has them before being
# imported by Alembic
# from app.db.base_class import Base  # noqa
#from db.base_class import Base  # noqa

# from app.models.notes import notes  # noqa

#import databases
#import orm
#import sqlalchemy
from db.base import database, metadata
from notes import models  # noqa
