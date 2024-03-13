import sys
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_first_state(username, password, database):
    # Create an engine to connect to MySQL server
    engine = sqlalchemy.create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')
    
    # Create a session factory
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()
    
    # Check if the table is empty
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")
    
    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    print_first_state(username, password, database)
