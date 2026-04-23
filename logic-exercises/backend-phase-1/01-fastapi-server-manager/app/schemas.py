from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel, Field, IPvAnyAddress, EmailStr

class UserSchema(BaseModel):
    username: Optional[str] = Field(min_length=3, max_length=20)
    email: Optional[EmailStr] 
    age: Optional[int] = None

class ServerCreate(BaseModel):
    hostname: str = Field(min_length=5)
    ip_address: IPvAnyAddress  
    cpu_cores: int = Field(..., gt=0)
    ram_gb: int
    is_active: bool = True

class ServerUpdate(BaseModel):
    hostname: Optional[str] = Field(None, min_length=5)
    ip_address: Optional[IPvAnyAddress] = None
    cpu_cores: Optional[int] = Field(None, gt=0)
    ram_gb: Optional[int] = None
    is_active: Optional[bool] = None

class ServerResponse(ServerCreate):
    id: UUID