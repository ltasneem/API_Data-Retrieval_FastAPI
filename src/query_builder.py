#import model classes
from models.personnel.GL_PersonProfile import *
from models.personnel.PersonProfileRequest import *
from models.personnel.PersonProfileResponse import *
from queries.PersonProfileQueries import *

from time import perf_counter

#dynamic join query
def populate_query_personnel_personProfile(param: PersonProfileRequest, engine : Engine):
  map_personnel_personProfile(param, engine)
  #result = personProfileResponseList
  result = PersonProfileResponseList
  try:
    if(param is not None):
      if(param.flag):
          PersonProfileResponseList = list[PersonProfileResponse] = PersonProfileQuery(param, engine)
          #result.PersonProfile = personProfileResponse
  except AttributeError:
    pass
  return result

def map_personnel_personProfile(param: PersonProfileRequest, engine : Engine):
  mapper_registry_personnel = registry(metadata=MetaData(schema='person_pub'))
  # if flag is on
  mapper_registry_personnel.map_imperatively(GL_PersonProfile_cls, create_GL_PerosnProfile(engine, mapper_registry_personnel))

def PersonProfileQuery(param: PersonProfileRequest, engine : Engine):
  personProfileResult = list[PersonProfileResponse] = []
  t1 = perf_counter()
  personProfileQuery = populate_personProfile_query(GL_PersonProfile_cls)
  personProfile = engine.execute(personProfileQuery)

  t3 = perf_counter()
  for obj in personProfile:
    personProfileResult.append(obj)
  t2 = perf_counter()
  print("Execution time for query")
  print(t2-t1)
  return personProfileResult
