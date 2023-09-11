from pyndantic import models


class Book(BaseModel):
    __tablename__="books"
    id:str
    title:str
    pages:int
    published_date:str



