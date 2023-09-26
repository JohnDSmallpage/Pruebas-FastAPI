from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    nombre: str
    email: str
    password: str