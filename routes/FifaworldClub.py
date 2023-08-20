# Create a backend for the Fifa World Cup app
# Import router from fastapi
from fastapi import APIRouter, Response, status
# Import the functions schema.FifaworldClub
from schema.FifaworldClub import get_one_fifa_world_club, get_all_fifa_world_club
# Import the functions config.db
from config.db import db
# Import models from FifaworldClub
from models.FifaworldClub import FifaWorldClub
# Import bson
from bson import ObjectId
# Import startlette status 204
from starlette.status import HTTP_204_NO_CONTENT


# Create an instance of APIRouter
router = APIRouter()

# Create a route get all clubs
@router.get('/clubs', response_model=list[FifaWorldClub], tags=["clubs"])
async def find_all_clubs():
    lista_clubs = list(db.FifaWorldClub.find())
    # print(list(db.FifaWorldClub.find()))
    return get_all_fifa_world_club(lista_clubs)

# Create a route post club
@router.post('/clubs', response_model=FifaWorldClub, tags=["clubs"])
async def create_club(club: FifaWorldClub):
    new_club = dict(club)
    del new_club["id"]
    id = db.FifaWorldClub.insert_one(new_club).inserted_id
    club_create = db.FifaWorldClub.find_one({"_id": id})
    return get_one_fifa_world_club(club_create)

# Create a route get one club
@router.get('/clubs/{id}', response_model=FifaWorldClub, tags=["clubs"])
async def find_user(id: str):
    return get_one_fifa_world_club(db.FifaWorldClub.find_one({"_id": ObjectId(id)}))

# Create a route put club (edit)
@router.put("/clubs/{id}", response_model=FifaWorldClub, tags=["clubs"])
async def update_user(id: str, club: FifaWorldClub):
    db.FifaWorldClub.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(club)
    })
    return get_one_fifa_world_club(db.FifaWorldClub.find_one({"_id": ObjectId(id)}))

# Create a route delete club (delete)
@router.delete("/clubs/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["clubs"])
async def delete_user(id: str):
    db.FifaWorldClub.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)
