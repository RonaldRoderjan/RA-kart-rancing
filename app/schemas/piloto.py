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

# NOVO SCHEMA: para receber dados na atualização de um piloto
# Todos os campos são opcionais
class PilotoUpdate(BaseModel):
    nome_completo: str | None = None
    apelido: str | None = None
    valor_mensalidade: float | None = None
    ativo: bool | None = None
    categoria_id: int | None = None

class Piloto(PilotoBase):
    piloto_id: int
    categoria: Categoria | None = None

class PiloroSummary (BaseModel):
    valor_mensalidade: float
    total_gastos: float 
    total_reembolsos: float
    valor_final_mes: float
