from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    credits = Column(Integer, default=1000) 
    created_at = Column(DateTime, default=datetime.utcnow)

    cards = relationship("PlayerCard", back_populates="owner")

class PlayerCard(Base):
    __tablename__ = "player_cards"

    id = Column(Integer, primary_key=True, index=True)
    
    # Stats
    player_name = Column(String)# e.g., "TenZ"
    team_name = Column(String)  # e.g., "Sentinels"
    player_role = Column(String) # e.g., "Duelist", "Controller"
    tier = Column(Integer)      # e.g., 1, 2, 3
    card_type = Column(String) # e.g., "Normal", "Masters: Reykjavik", "Champions: Istanbul"

    mechanics = Column(Float, default=0.0)
    game_sense = Column(Float, default=0.0)
    consistency = Column(Float, default=0.0)
    clutch_factor = Column(Float, default=0.0)
    leadership = Column(Float, default=0.0)

    # Foreign Key to link to User
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="cards")

    