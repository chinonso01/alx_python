import sys
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import func

def list_states_with_letter_a(username, password, database):
    # Create an engine to connect to MySQL server
    engine = sqlalchemy.create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')
    
    # Create a session factory
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Query State objects containing the letter 'a' and sort them by id
    states_with_a = session.query(State).filter(func.lower(State.name).like('%a%')).order_by(State.id).all()
    
    # Print the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    list_states_with_letter_a(username, password, database)
