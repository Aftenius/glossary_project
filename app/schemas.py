from pydantic import BaseModel

class TermBase(BaseModel):
    keyword: str
    description: str

class TermCreate(TermBase):
    pass

class TermUpdate(TermBase):
    pass

class TermResponse(TermBase):
    id: int

    class Config:
        orm_mode = True
