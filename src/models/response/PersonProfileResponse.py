from pydantic import BaseModel

Class PersonProfileResponse(BaseModel):
  personId: int
  name: str
  location: str
  age: int
