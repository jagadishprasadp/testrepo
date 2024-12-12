from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from . import models
from . import schemas
app = FastAPI()
from .database import engine, SessionLocal

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield
    finally:
        db.close()

@app.post('/task')
def blog_task(request: schemas.BlogModel,db:Session =Depends(get_db)):
    new_blog = models.BlogsTable(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog