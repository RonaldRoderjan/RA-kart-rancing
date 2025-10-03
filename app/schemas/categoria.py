# app/schemas/categoria.py
from pydantic import BaseModel

class Categoria(BaseModel):
    categoria_id: int
    nome_categoria: str
    # A 'class Config' foi removida