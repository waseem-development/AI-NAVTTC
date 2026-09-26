from pydantic import BaseModel # type: ignore
from typing import List, Dict, Optional

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

