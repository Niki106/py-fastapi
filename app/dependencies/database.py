from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql+mysqldb://root:@localhost/test"
# DATABASE_URL = "postgresql://postgres:glowglow@localhost:5432/salesorder"
DATABASE_URL = "postgresql://doadmin:AVNS_OPaHDSDw7xOgi5H-yfl@db-postgresql-nyc3-28362-do-user-18300103-0.i.db.ondigitalocean.com:25060/defaultdb"

db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
