from fastapi import FastAPI
from models.user_connection import UserConnection
from schema.users_schema import UserSchema

app = FastAPI()
conn= UserConnection()

@app.get("/")
def root():
    conn
    return {"message": "Hello World during the coronavirus pandemic!"}

@app.post("/api/insert")
def insert(user_data:UserSchema):
    data = user_data.dict()
    conn.write(data)
