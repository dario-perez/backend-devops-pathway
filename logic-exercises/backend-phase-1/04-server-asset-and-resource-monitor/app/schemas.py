from uuid import UUID
from typing import Optional, Literal

from pydantic import BaseModel, IPvAnyAddress, Field

class Asset(BaseModel):
    id: UUID
    hostname: str
    ip_address: IPvAnyAddress
    status: Optional[Literal["Online", "Offline", "Maintenance"]] = "Online"
    cpu_usage: float = Field(ge=0, le=100)
    ram_usage: float = Field(ge=0, le=100)