from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Finding database Url
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

#create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declare mapping
Base = declarative_base()