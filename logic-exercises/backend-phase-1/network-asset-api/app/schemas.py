from uuid import UUID
from pydantic import BaseModel, IPvAnyAddress, Field

class NetworkAsset(BaseModel):
    id: UUID
    hostname: str
    ip_address: IPvAnyAddress
    ram_gb: int = Field(gt=0)