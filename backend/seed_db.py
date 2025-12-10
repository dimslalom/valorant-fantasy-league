from .database import SessionLocal
from .models import User, PlayerCard

def seed_data():
    print("Starting seed process...")

    # Create a new database session
    db = SessionLocal()

    # Check if users already exist
    existing_users = db.query(User).filter(User.username == "dimslalom").first()
    if existing_users:
        print("Seed data already exists. Skipping seeding.")
        db.close()
        return
    
    # Create a sample user
    new_user = User(
        username="dimslalom",
        email="dimas@admin.com",
        credits=1500
    )


    # Create a Card (Tenz - Sentinels - Duelist - Tier 2 - Masters: Reykjavik)
    tenz_card = PlayerCard(
        player_name="TenZ",
        team_name="Sentinels",
        player_role="Duelist",
        tier=2,
        card_type="Masters: Reykjavik",
        mechanics=90.0,
        game_sense=90.0,
        consistency=80.0,
        clutch_factor=75.0,
        leadership=70.0,
    )
    
    # Append this card to the user's cards
    new_user.cards.append(tenz_card)

    # Save to the database
    db.add(new_user)
    db.commit()

    print("✅ Seed data inserted successfully.")

    db

if __name__ == "__main__":
    seed_data()