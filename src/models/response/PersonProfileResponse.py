from pydantic import BaseModel

Class PersonProfileResponse(BaseModel):
  personId: int
  name: int
  location: str
  age: int
