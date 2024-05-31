from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Double, DateTime, Enum
from app.dependencies.database import Base
import enum

class PayType(str, enum.Enum):
    cash = "Cash"
    card = "Card"

class SalesOrdeInfo(Base):
    __tablename__ = "salesorders"

    id = Column(Integer, primary_key=True, index=True)
    orderNumber = Column(String)
    customerID = Column(Integer)
    orderDate = Column(DateTime)
    status = Column(Integer)
    totalAmount = Column(Double)
    payType = Column(Enum(PayType))
