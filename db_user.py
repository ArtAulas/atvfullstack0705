from sqlalchemy import Column, SmallInteger, String, Date
from pydantic import BaseModel
from db_config import Base
from datetime import date

#ORM-definir a tabela no banco de dados
class Usuario(Base):
    __tablename__='usuarios'
    id=Column('id',SmallInteger, primary_key=True, autoincrement=True)
    nome=Column('nome',String(16))
    email=Column('email',String(50))
    telefone=Column('telefone',String(12))
    dt_nasc=Column('dt_nasc', Date)

#schemas-utilizar para response e request
class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str
    dt_nasc: date

    class Config:
        from_attributes=True

class UsuarioRequest(BaseModel):
    nome:str
    email: str
    telefone: str
    dt_nasc:date