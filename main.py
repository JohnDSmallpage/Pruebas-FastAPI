from fastapi import FastAPI, Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_201_CREATED
from models.user_connection import UserConnection
from schema.users_schema import UserSchema
from schema.users_schema import UserSchemaUpdate

app = FastAPI()
conn= UserConnection()

@app.get("/", status_code=HTTP_200_OK)
def root():
    items = []
    dictionary = {}
    for data in conn.read_all():
        dictionary = {
            "id": data[0],
            "nombre": data[1],
            "email": data[2],
            "password": data[3]
        }
        items.append(dictionary)
    return items

@app.get("/api/{email}" , status_code=HTTP_200_OK)
def get_one(email:str):
    item = []
    data = conn.read_one(email)
    dictionary= {
        "id": data[0],
        "nombre": data[1],
        "email": data[2],
        "password": data[3]
    }
    item.append(dictionary)
    return item

@app.delete("/api/delete/{email}", status_code=HTTP_204_NO_CONTENT)
def delete(email:str):
    conn.delete(email)
    return Response(status_code=HTTP_204_NO_CONTENT)

@app.post("/api/insert", status_code=HTTP_201_CREATED)
def insert(user_data:UserSchema):
    data = user_data.dict()
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@app.put("/api/update/{email}", status_code=HTTP_200_OK)
def update(email:str, user_data:UserSchemaUpdate):
    data = user_data.dict()
    data["email"] = email
    conn.update(data)
    return f"Usuario {email} actualizado"

