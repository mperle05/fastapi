from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from passlib.context import CryptContext
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models,schema, utils
from .database import engine, get_db
from typing import Optional, List
from .routers import post, user, auth



app = FastAPI()

models.Base.metadata.create_all(bind = engine)




my_posts = [{"title" : "title post 1", "content": "content post 1", "id": 1}]

while True:
    try: 
        conn = psycopg2.connect(host = 'localhost', database ='fastapi', user = 'postgres', 
                                password = 'q2NfjBn8Y6Un7n', cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database succesfull")
        break
    except Exception as error:  
        print("databese failed.")
        print("Error:", error)
        time.sleep(2)









def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def root():
    return {"message": "Hello API  "}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)



