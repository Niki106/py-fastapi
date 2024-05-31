from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.schemas.salesorder import SalesOrder4CU, SalesOrder, PaginatedSalesOrderInfo
from app.crud.salesorder import get_all_orders, get_order_by_id, create_order, update_order_by_id, delete_order_by_id
from app.dependencies.exceptions import SalesOrderException

router = APIRouter()

@cbv(router)
class SalesOrders:
    session: Session = Depends(get_db)

    @router.get("/salesorders", response_model=PaginatedSalesOrderInfo)
    def list_orders(self, limit: int = 10, offset: int = 0):
        order_list = get_all_orders(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": order_list}

        return response 

    # API endpoint to add a car info to the database
    @router.post("/salesorders")
    def add_order(self, sales_order: SalesOrder4CU):
        try:
            sales_order = create_order(self.session, sales_order)
            return sales_order
        except SalesOrderException as cie:
            raise HTTPException(**cie.__dict__)   

# API endpoint to get info of a particular sales order
@router.get("/salesorders/{order_id}", response_model=SalesOrder)
def get_order(car_id: int, session: Session = Depends(get_db)):

    try:
        sales_order = get_order_by_id(session, car_id)
        return sales_order
    except SalesOrderException as cie:
        raise HTTPException(**cie.__dict__)

# API to update a existing sales order
@router.put("/salesorders/{order_id}", response_model=SalesOrder)
def update_order(order_id: int, new_info: SalesOrder4CU, session: Session = Depends(get_db)):
    try:
        car_info = update_order_by_id(session, order_id, new_info)
        return car_info
    except SalesOrderException as cie:
        raise HTTPException(**cie.__dict__)

# API to delete a car info from the data base
@router.delete("/salesorders/{order_id}")
def delete_order(order_id: int, session: Session = Depends(get_db)):
    try:
        return delete_order_by_id(session, order_id)
    except SalesOrderException as cie:
        raise HTTPException(**cie.__dict__)