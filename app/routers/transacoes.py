from fastapi import APIRouter, HTTPException, status
from app.schemas.transacao import Transacao, TransacaoCreate
from app.db import crud_transacoes

router = APIRouter(
prefix="/transacoes",
tags=["transacoes"]
)    

@router.post("/", response_model=Transacao, status_code=status.HTTP_201_CREATED)
def create_new_transacao(transacao: TransacaoCreate):
    db_transacao = crud_transacoes.create_transacao(transacao=transacao)
    if db_transacao is None:
        raise HTTPException(status_code=500, detail="Erro ao criar a transação")
    return db_transacao