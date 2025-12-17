import pytest
from sqlalchemy import create_engine, select, MetaData
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker, registry, clear_mappers

from src.models import *
from src.core_common.src.connection import engine

from typing import Any, List
mapper_registry_personnel = registry(metadata=MetaData(schema='personnel'))

@pytest.fixture(scope='function')
def session():
  session_maker = sessionmaker(bind=engine, future=True)
  session = session_maker()
  clear_mappers()
  yield session
  session.rollback()

def test_engine():
  assert (enginer is not None) == True

@pytest.mark.skip(reason="skip testing this")
def test_person_profile_model(session: Session):
  mapper_registry_personnel.map_imperatively(GL_PersonProfile_cls, create_GL_PersonProfile(engine, mapper_registry_personnel))
  stmt = select(PersonProfile_cls).where(PersonProfile_cls.PersonId == 268)
  testList = List[GL_PersonProfile_cls] = session.execute(stmt).scalars().all()
  print(len(testList))
  assert len(testList) >= 0
