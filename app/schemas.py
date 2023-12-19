from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class UserResponse(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool
    owner: UserResponse

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int

class PostOut(BaseModel):
    Post: Post
    votes: int

class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
