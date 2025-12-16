from sqlalchemy.orm import registry
from sqlalchemy.engine import Engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from pydantic import BaseModel

class GL_PersonProfile_cls:
    pass
def create_GL_PersonProfile(engine: Engine, mapper_registry: registry)
    GL_PersonProfile = Table(
    "GL_PersonProfile", mapper_registry.metadata,
    Column("personId", Integer, primary_key=True),
    Column("name", String),
    Column("location", String),
    Column("age", Integer),
    )
    return GL_PersonProfile
