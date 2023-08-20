# Import pydantic
from pydantic import BaseModel
from typing import Optional


'''
# Create a class userFifaClub
class userFifaWorldClub(BaseModel):
    id : Optional[str]
    name: str
    email: str
    password: str
    img: str
'''

# Create a class FifaWorldClub


class FifaWorldClub(BaseModel):
    id: Optional[str]
    name: str
    country: str
    continent: str
    club: str
    year: int
    position: int
    points: int
    goals: int
    image: Optional[str]
