from pydantic import BaseModel
from enum import Enum
from datetime import date

class TipoTransacao(str,Enum):
    gastos_extras = "GASTO_EXTRA"
    reembolso = "REEMBOLSO"
    mensalidade = "MENSALIDADE"

class TransacaoBase(BaseModel):
    descricao: str 
    valor: float
    tipo: TipoTransacao

class TransacaoCreate(TransacaoBase):
    piloto_id: int
    data_transacao: date = date.today()

class Transacao(TransacaoBase):
    transacao_id: int
    piloto_id: int
    data_transacao: date