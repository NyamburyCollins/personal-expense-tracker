from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base

# Create the SQLite engine
engine = create_engine('sqlite:///expenses.db')

# Bind the engine to a session
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables based on the Base metadata
Base.metadata.create_all(engine)
