from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.piloto import Piloto, PilotoCreate, PilotoUpdate  # Importa nosso novo schema
from app.db import crud_pilotos
from app.schemas.transacao import Transacao
from app.db import crud_transacoes

router = APIRouter(
    prefix="/pilotos",
    tags=["Pilotos"] # Agrupa os endpoints na documentação
)

@router.get("/", response_model=List[Piloto])
def read_pilotos():
    pilotos = crud_pilotos.get_all_pilotos()
    if pilotos is None:
        raise HTTPException(status_code=500, detail="Erro ao buscar pilotos.")
    return pilotos

@router.post("/",response_model=Piloto, status_code=status.HTTP_201_CREATED)
def create_new_piloto(piloto: PilotoCreate):
    db_piloto = crud_pilotos.create_piloto(piloto=piloto)
    if db_piloto is None:
        raise HTTPException(status_code=500, detail="Erro ao criar o piloto.")
    
    all_Pilots = crud_pilotos.get_all_pilotos()
    novo_piloto_completo = next ((p for p in all_pilots if p['piloto_id'] == db_piloto['piloto_id']), None)

    return novo_piloto_completo

@router.put ("/{piloto_id}", response_model=Piloto)
def update_existing_piloto(piloto_id: int, piloto: PilotoUpdate):
    updated_piloto = crud_pilotos.update_piloto(piloto_id=piloto_id, piloto=piloto)
    if updated_piloto is None:
        raise HTTPException(status_code=500, detail= "Erro ao atualizar o piloto.")

    all_pilots = crud_pilotos.get_all_pilotos()
    piloto_completo = next ((p for p in all_pilots if p['piloto_id'] == piloto_id), None) 

    if piloto_completo is None:
        raise HTTPException(status_code=404, detail="Piloto não encontrado após a atualização. ")

    return piloto_completo

@router.delete("/{piloto_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_piloto(piloto_id: int):
    success = crud_pilotos.delete_piloto(piloto_id=piloto_id)
    if not success:
        raise HTTPException(status_code=404, detail="Piloto não encontrado.")
    return

@router.get("/{piloto_id}/transacoes", response_model=List[Transacao], tags=["Plotos"])
def read_transacoes_for_piloto(piloto_id: int):
    transacoes = crud_transacoes.get_transacoes_by_piloto(piloto_id=piloto_id)
    if transacoes is None:
        raise HTTPException(status_code=500, detail="Erro ao buscar transações do piloto.")
    return transacoes