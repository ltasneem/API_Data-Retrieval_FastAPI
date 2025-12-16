from pydantic import BaseModel

Class PersonProfileRequest(BaseModel):
  personId: int
  name: str
  location: str
  age: int
