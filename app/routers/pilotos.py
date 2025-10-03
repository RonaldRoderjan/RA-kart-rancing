# app/routers/pilotos.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.piloto import Piloto # Importa nosso novo schema
from app.db import crud_pilotos

router = APIRouter(
    prefix="/pilotos",
    tags=["Pilotos"] # Agrupa os endpoints na documentação
)

@router.get("/", response_model=List[Piloto])
def read_pilotos():
    pilotos = crud_pilotos.get_all_pilotos()
    if pilotos is None:
        raise HTTPException(status_code=500, detail="Erro ao buscar pilotos.")

    # O Pydantic vai validar e formatar os dados de acordo com o schema Piloto
    return pilotos