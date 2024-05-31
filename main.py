# main.py
# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from app.routers import salesorder 

import os
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

# Initialize the app
app = FastAPI()

app.include_router(salesorder.router)


# GET operation at route '/'
@app.get('/')
async def root_api():
    return {"message": "Welcome to Balasundar's Technical Blog"}
