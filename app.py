# Import fastApi
from fastapi import FastAPI
# Import the router from routes/FifawordClub.py
from routes.FifaworldClub import router as fifaWorldClubRouter
# Import cors
from fastapi.middleware.cors import CORSMiddleware

# Create an instance of FastAPI
app = FastAPI(
    title="Fifa World Club App",
    description="This is a backend for the Fifa World Club App",
    version="1.0.0"
)

# Add cors
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
]

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"]
)

# Create a route
@app.get("/")
def index():
    return {"Title pag": "Fifa World Club App"}


# Register the router
app.include_router(fifaWorldClubRouter)

# Run the app with unicorn server personalization
# if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=3000)
