from fastapi import FastAPI
from pydantic import BaseModel





class Book(BaseModel):
    __tablename__="books"
    id:int
    title:str
    body:str
    published_year:str



