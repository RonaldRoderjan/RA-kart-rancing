# app/schemas/piloto.py
from pydantic import BaseModel
from app.schemas.categoria import Categoria

class PilotoBase(BaseModel):
    nome_completo: str
    apelido: str | None = None
    valor_mensalidade: float
    ativo: bool

class PilotoCreate(PilotoBase):
    categoria_id: int

class Piloto(PilotoBase):
    piloto_id: int
    categoria: Categoria | None = None
    # A 'class Config' foi removida