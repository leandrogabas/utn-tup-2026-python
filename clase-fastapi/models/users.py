from typing import List, Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    is_active: bool = True


class UserUpdate(BaseModel):
    name: str = Field(..., min_length=1)
    is_active: bool


class UserPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    is_active: Optional[bool] = None


class GetUsersResponse(BaseModel):
    users: List[User]


class CreateUserResponse(BaseModel):
    message: str


class UpdateUserResponse(BaseModel):
    message: str
    user: User


class DeleteUserResponse(BaseModel):
    message: str
