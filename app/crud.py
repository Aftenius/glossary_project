from sqlalchemy.orm import Session
from app import models, schemas

def get_terms(db: Session):
    return db.query(models.Term).all()

def get_term_by_keyword(db: Session, keyword: str):
    return db.query(models.Term).filter(models.Term.keyword == keyword).first()

def create_term(db: Session, term: schemas.TermCreate):
    db_term = models.Term(keyword=term.keyword, description=term.description)
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term

def update_term(db: Session, term: schemas.TermUpdate, keyword: str):
    db_term = get_term_by_keyword(db, keyword)
    if db_term:
        db_term.description = term.description
        db.commit()
        db.refresh(db_term)
    return db_term

def delete_term(db: Session, keyword: str):
    db_term = get_term_by_keyword(db, keyword)
    if db_term:
        db.delete(db_term)
        db.commit()
    return db_term