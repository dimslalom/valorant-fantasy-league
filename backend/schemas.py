from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PlayerCardSchema(BaseModel):
    id: int
    player_name: str
    team_name: str
    player_role: str
    tier: int
    card_type: str
    mechanics: float
    game_sense: float
    consistency: float
    clutch_factor: float
    leadership: float
    owner_id: Optional[int]

    # This config tells Pydantic to treat SQlAlchemy models as dicts
    class Config:
        from_attributes = True

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    credits: int
    created_at: datetime

    # Include related player cards
    cards: List[PlayerCardSchema] = []

    class Config:
        from_attributes = True