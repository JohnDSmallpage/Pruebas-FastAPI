from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    nombre: str
    email: str
    password: str

class UserSchemaUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None