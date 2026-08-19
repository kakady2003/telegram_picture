import uuid

from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreateSchemas(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    email: EmailStr
    password: str




class UserReadSchemas(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    username: str
    email: EmailStr
