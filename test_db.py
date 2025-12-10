from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# 1. The Connection String
# Syntax: postgresql://<username>:<password>@<host>:<port>/<database_name>
DATABASE_URL = "postgresql://admin:password123@localhost:5433/valorant_fantasy"

# 2. Create the "Engine"
# The engine is the starting point for any SQLAlchemy application.
# It manages the pool of connections to the database.
engine = create_engine(DATABASE_URL)

def test_connection():
    try:
        # 3. Open a connection
        with engine.connect() as connection:
            # 4. Run a simple SQL command
            # "SELECT 1" is the standard way to ping a database to see if it's alive.
            result = connection.execute(text("SELECT 1"))
            
            # 5. Check the result
            print("\n---------------------------------------------------")
            print("✅ SUCCESS: Connected to the database!")
            print(f"   Test Query Result: {result.scalar()}") 
            print("---------------------------------------------------\n")
            
    except OperationalError as e:
        print("\n---------------------------------------------------")
        print("❌ ERROR: Could not connect.")
        print("   Is Docker running? Did you run 'docker-compose up'?")
        print(f"   Details: {e}")
        print("---------------------------------------------------\n")

if __name__ == "__main__":
    test_connection()