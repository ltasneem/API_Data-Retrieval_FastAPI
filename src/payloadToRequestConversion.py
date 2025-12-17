from sqlalchemy.orm import clear_mappers
import json


def personProfileRequestConversion(payloadconverted: str):
  json_object = json.loads(payloadconverted)
  #parsing the request
  clear_mappers()
  request =PersonProfileRequest
  
  return request
