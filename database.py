from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "sqlite:///./fastapi.db"
metadata = MetaData(
    naming_convention={
        "ix": 'ix_%(column_0_label)s',  # Index naming convention
        "uq": "uq_%(table_name)s_%(column_0_name)s",  # Unique constraint naming convention
        "ck": "ck_%(table_name)s_%(constraint_name)s",  # Check constraint naming convention
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",  # Foreign key naming convention
        "pk": "pk_%(table_name)s"  # Primary key naming convention
    }
)
engine = create_engine(url=DATABASE_URI, connect_args={"check_same_thread": False})
Base = declarative_base(metadata=metadata)
Session = sessionmaker(bind=engine, autocommit=False, expire_on_commit=False, autoflush=False)
session = Session()


def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()


def create_db():
    Base.metadata.create_all(bind=engine)
