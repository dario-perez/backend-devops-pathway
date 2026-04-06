from pydantic import BaseModel, Field, IPvAnyAddress, EmailStr
from typing import Optional

class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr 
    age: Optional[int] = None

class ServerCreate(BaseModel):
    hostname: str = Field(min_length=5)
    ip_address: IPvAnyAddress  
    cpu_cores: int = Field(..., gt=0)
    ram_gb: int
    is_active: bool = True
