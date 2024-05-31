from pydantic import BaseModel
from datetime import datetime
from app.models.salesorder import PayType
from typing import Optional, List

class SalesOrder4CU(BaseModel):
    orderNumber: str
    customerID: int
    orderDate: datetime
    status: int
    totalAmount: float
    payType: PayType

class SalesOrderItem(BaseModel):
    salesOrderID: int
    productID: int
    quantity: int
    unitPrice: float
    status: int
    totalPrice: float

# TO support list and get APIs
class SalesOrder(SalesOrder4CU):
    id: int

    class Config:
        orm_mode = True

# To support list salesorder API
class PaginatedSalesOrderInfo(BaseModel):
    limit: int
    offset: int
    data: List[SalesOrder]