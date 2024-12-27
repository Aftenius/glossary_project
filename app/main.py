from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, schemas, crud

# Создаем базу данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/terms/", response_model=list[schemas.TermResponse])
def read_terms(db: Session = Depends(get_db)):
    return crud.get_terms(db)

@app.get("/terms/{keyword}", response_model=schemas.TermResponse)
def read_term(keyword: str, db: Session = Depends(get_db)):
    term = crud.get_term_by_keyword(db, keyword)
    if term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return term

@app.post("/terms/", response_model=schemas.TermResponse)
def create_term(term: schemas.TermCreate, db: Session = Depends(get_db)):
    db_term = crud.get_term_by_keyword(db, term.keyword)
    if db_term:
        raise HTTPException(status_code=400, detail="Keyword already exists")
    return crud.create_term(db, term)

@app.put("/terms/{keyword}", response_model=schemas.TermResponse)
def update_term(keyword: str, term: schemas.TermUpdate, db: Session = Depends(get_db)):
    return crud.update_term(db, term, keyword)

@app.delete("/terms/{keyword}", response_model=schemas.TermResponse)
def delete_term(keyword: str, db: Session = Depends(get_db)):
    term = crud.delete_term(db, keyword)
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")
    return term