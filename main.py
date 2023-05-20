from fastapi import FastAPI
from sqlalchemy.orm import declarative_base

from auth import authentication
from db import models
from db.database import engine
from router import user, profile

Base = declarative_base()
app = FastAPI()


@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(engine)


app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(profile.router)


@app.get('/hello')
def index():
    return {'message': 'Hello world!'}
