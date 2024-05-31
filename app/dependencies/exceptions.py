# exceptions.py
class SalesOrderException(Exception):
    ...


class SalesOrderNotFoundError(SalesOrderException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Sales Order Not Found"


class SalesOrderAlreadyExistError(SalesOrderException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Sales Order Already Exists"
