from pydantic import BaseModel

Class PersonProfileRequest(BaseModel):
  personId: int
  name: int
  location: str
  age: int
