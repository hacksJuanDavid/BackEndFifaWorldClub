'''
# Create function get one user fifa world club
def get_one_user_fifa_world_club(item) -> dict:
    return {"data": {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"],
        "img": item["img"]
    }}

# Create function get all user fifa world club
def get_all_user_fifa_world_club(items) -> list:
    return [get_one_user_fifa_world_club(item) for item in items]
'''

# Create function to get one the fifa world club


def get_one_fifa_world_club(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "country": item["country"],
        "continent": item["continent"],
        "club": item["club"],
        "year": item["year"],
        "position": item["position"],
        "points": item["points"],
        "goals": item["goals"],
        "image": str(item["image"]) 
    }


# Create function to get all the fifa world club


def get_all_fifa_world_club(items) -> list:
    return [get_one_fifa_world_club(item) for item in items]
