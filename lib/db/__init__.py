from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///fitness.db"

#create engine
engine = create_engine(DATABASE_URL)
#Session factory
SessionLocal = sessionmaker(bind=engine)
#Base
Base = declarative_base()