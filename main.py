from fastapi import FastAPI
from sqlalchemy.orm import declarative_base

from db import models
from db.database import engine
from router import user

Base = declarative_base()
app = FastAPI()


@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(engine)


app.include_router(user.router)


@app.get('/hello')
def index():
    return {'message': 'Hello world!'}
