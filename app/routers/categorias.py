# app/routers/categorias.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.categoria import Categoria
from app.db import crud_categorias

# A variável DEVE se chamar 'router' para o main.py encontrá-la
router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)

@router.get("/", response_model=List[Categoria])
def read_categorias():
    categorias = crud_categorias.get_all_categorias()
    if categorias is None:
        raise HTTPException(status_code=500, detail="Erro ao buscar categorias no banco de dados.")
    return categorias