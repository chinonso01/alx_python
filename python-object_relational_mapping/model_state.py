import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """
    Represents a state entity in the MySQL table 'states'.
    
    Attributes:
        id (int): An auto-generated, unique integer representing the primary key.
        name (str): A string representing the name of the state, with a maximum of 128 characters.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# If you have multiple classes, make sure to import them all before calling Base.metadata.create_all(engine)
# For example:
# from another_module import AnotherClass

if __name__ == "__main__":
    # This part will only be executed when you run this script directly, not when imported
    
    # Create an engine to connect to MySQL server
    engine = sqlalchemy.create_engine('mysql://<username>:<password>@localhost:3306/<database>')
    
    # Create all tables defined by Base classes
    Base.metadata.create_all(engine)
