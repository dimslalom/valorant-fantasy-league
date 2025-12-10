from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from .database import SessionLocal, engine
from .models import User
from .schemas import UserSchema

#initialize the app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Valorant Fantasy League API!"}

# Endpoint to get user by their ID
@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    # Query the user from the database
    # joinedload to fetch related PlayerCards in the same query
    user = db.query(User).options(joinedload(User.cards)).filter(User.id == user_id).first()

    # Check if user exists
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Return user data
    return user

