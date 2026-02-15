from pydantic import BaseModel
from typing import Optional

class MenuItemCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str
    available: bool

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    available: Optional[bool] = None

class MenuItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str
    available: bool

    class Config:
        from_attributes = True
