# In models/order.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float


class CustomerInfo(BaseModel):
    name: str
    email: EmailStr
    address: Optional[str] = None
    phone: Optional[str] = None


class Order(BaseModel):
    order_id: str
    customer: CustomerInfo
    items: List[OrderItem]
    total: float
    order_date: datetime = datetime.now()
    shipping_method: Optional[str] = None
    estimated_delivery: Optional[datetime] = None
    notes: Optional[str] = None