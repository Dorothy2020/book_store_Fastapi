from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_books():
    return{"message":"My very first book store api"}