from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Dict
from uuid import uuid4    # uuid4 generates unique user IDs

#  use this command to Run the code:  uvicorn main:app --reload 

app = FastAPI()   # Create a FastAPI app instance
users: Dict[str, dict] = {}   # In-memory storage for users, keyed by user_id (string)

class User(BaseModel):    # Pydantic model for validating incoming user data
    name: str
    email: EmailStr


@app.get("/")          # GET endpoint to check if API is running
def api_running():
    return {"id": "API is perfectly running"}

@app.post("/users")                 # POST endpoint to create a new user
def create_user(user: User):
    user_id = str(uuid4())          # Generate a unique user ID
    users[user_id] = user.dict()    # Convert User model to dictionary and store it
    return {"id": user_id, **users[user_id]}  # Return the created user's data with ID

@app.get("/users/{user_id}")       # GET endpoint to retrieve a user by ID
def get_user(user_id: str):
    if user_id not in users:       # Check if user exists
        raise HTTPException(status_code=404, detail="User not found")  # Return 404 if not found
    return {"id": user_id, **users[user_id]}    # Return user data

@app.put("/users/{user_id}")    # PUT endpoint to update an existing user
def update_user(user_id: str, user: User):
    if user_id not in users:              # Check if user exists
        raise HTTPException(status_code=404, detail="User not found")  # Return 404 if not found
    users[user_id] = user.dict()          # Replace existing user data with new data
    return {"id": user_id, **users[user_id]}  # Return updated user data

@app.delete("/users/{user_id}")       # DELETE endpoint to remove a user by ID
def delete_user(user_id: str):
    if user_id not in users:          # Check if user exists
        raise HTTPException(status_code=404, detail="User not found")  # Return 404 if not found
    del users[user_id]                # Delete user from dictionary
    return {"detail": "User deleted"}     # Confirm deletion
