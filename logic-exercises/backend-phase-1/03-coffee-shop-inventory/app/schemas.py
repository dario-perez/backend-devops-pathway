from uuid import UUID
from typing import Literal
from pydantic import BaseModel, Field

class Product(BaseModel):
    id: UUID
    name: str
    price: int = Field(gt=0)
    category: Literal["Coffee", "Food", "Equipment"]
    stock: int = Field(ge=0)