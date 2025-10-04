# app/routers/pilotos.py
from fastapi import APIRouter, HTTPException, status
from typing import List
from app.db import crud_categorias, crud_pilotos, crud_transacoes # Adicionei os outros cruds aqui para o futuro
from app.schemas.piloto import Piloto, PilotoCreate, PilotoUpdate, PilotoSummary
from app.schemas.transacao import Transacao

router = APIRouter(
    prefix="/pilotos",
    tags=["Pilotos"]
)

# Rota de Listagem (GET /pilotos/)
@router.get("/", response_model=List[Piloto])
def read_pilotos():
    pilotos = crud_pilotos.get_all_pilotos()
    if pilotos is None:
        raise HTTPException(status_code=500, detail="Erro ao buscar pilotos.")
    return pilotos

# Rota de Criação (POST /pilotos/)
@router.post("/", response_model=Piloto, status_code=status.HTTP_201_CREATED)
def create_new_piloto(piloto: PilotoCreate):
    # ... (código que já fizemos)
    db_piloto = crud_pilotos.create_piloto(piloto=piloto)
    if db_piloto is None:
        raise HTTPException(status_code=500, detail="Erro ao criar o piloto.")
    all_pilots = crud_pilotos.get_all_pilotos()
    novo_piloto_completo = next((p for p in all_pilots if p['piloto_id'] == db_piloto['piloto_id']), None)
    return novo_piloto_completo

# ROTA NOVA - GET /pilotos/{piloto_id}/summary
@router.get("/{piloto_id}/summary", response_model=PilotoSummary)
def read_piloto_summary(piloto_id: int):
    summary_data = crud_pilotos.get_piloto_summary(piloto_id=piloto_id)
    if summary_data is None:
        raise HTTPException(status_code=404, detail="Piloto não encontrado ou erro ao calcular resumo.")
    return summary_data

# ROTA NOVA - GET /pilotos/{piloto_id}/transacoes
@router.get("/{piloto_id}/transacoes", response_model=List[Transacao])
def read_transacoes_do_piloto(piloto_id: int):
    transacoes = crud_transacoes.get_transacoes_by_piloto(piloto_id=piloto_id)
    if transacoes is None:
        raise HTTPException(status_code=500, detail="Erro ao buscar transações.")
    return transacoes

# Rota de Atualização (PUT /pilotos/{piloto_id})
@router.put("/{piloto_id}", response_model=Piloto)
def update_existing_piloto(piloto_id: int, piloto: PilotoUpdate):
    # ... (código que já fizemos)
    crud_pilotos.update_piloto(piloto_id=piloto_id, piloto=piloto)
    all_pilots = crud_pilotos.get_all_pilotos()
    piloto_completo = next((p for p in all_pilots if p['piloto_id'] == piloto_id), None)
    if piloto_completo is None:
        raise HTTPException(status_code=404, detail="Piloto não encontrado.")
    return piloto_completo

# Rota de Deleção (DELETE /pilotos/{piloto_id})
@router.delete("/{piloto_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_piloto(piloto_id: int):
    # ... (código que já fizemos)
    success = crud_pilotos.delete_piloto(piloto_id=piloto_id)
    if not success:
        raise HTTPException(status_code=404, detail="Piloto não encontrado.")
    return