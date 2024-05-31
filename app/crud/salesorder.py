# crud.py
from typing import List
from sqlalchemy.orm import Session
from app.dependencies.exceptions import SalesOrderAlreadyExistError, SalesOrderNotFoundError
from app.models.salesorder import SalesOrdeInfo
from app.schemas.salesorder import SalesOrder4CU, SalesOrderItem, SalesOrder, PaginatedSalesOrderInfo


# Function to get list of sales order
def get_all_orders(session: Session, limit: int, offset: int) -> List[SalesOrdeInfo]:
    return session.query(SalesOrdeInfo).offset(offset).limit(limit).all()

# Function to  get info of a particular sales order
def get_order_by_id(session: Session, _id: int) -> SalesOrdeInfo:
    sales_order = session.query(SalesOrdeInfo).get(_id)

    if sales_order is None:
        raise SalesOrderNotFoundError

    return sales_order

# Function to add a new car info to the database
def create_order(session: Session, salesOrder: SalesOrder4CU) -> SalesOrdeInfo:
    car_details = session.query(SalesOrdeInfo).filter(SalesOrdeInfo.orderNumber == salesOrder.orderNumber, SalesOrdeInfo.customerID == salesOrder.customerID).first()
    if car_details is not None:
        raise SalesOrderAlreadyExistError

    new_sales_order = SalesOrdeInfo(**salesOrder.dict())
    session.add(new_sales_order)
    session.commit()
    session.refresh(new_sales_order)
    return new_sales_order


# Function to update details of the car
def update_order_by_id(session: Session, _id: int, info_update: SalesOrder4CU) -> SalesOrdeInfo:
    sales_order = get_order_by_id(session, _id)

    if sales_order is None:
        raise SalesOrderNotFoundError

    sales_order.orderNumber = info_update.orderNumber
    sales_order.customerID = info_update.customerID
    sales_order.orderDate = info_update.orderDate
    sales_order.status = info_update.status
    sales_order.totalAmount = info_update.totalAmount
    sales_order.payType = info_update.payType

    session.commit()
    session.refresh(sales_order)

    return sales_order


# Function to delete a car info from the db
def delete_order_by_id(session: Session, _id: int):
    sales_order = get_order_by_id(session, _id)

    if sales_order is None:
        raise SalesOrderNotFoundError

    session.delete(sales_order)
    session.commit()

    return
