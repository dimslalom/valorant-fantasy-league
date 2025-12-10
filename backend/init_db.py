from database import engine, Base
from models import User, PlayerCard

def init_db():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized with all tables.")

if __name__ == "__main__":
    init_db()