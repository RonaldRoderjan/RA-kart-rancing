# app/main.py
from fastapi import FastAPI
from app.routers import categorias, pilotos # <-- 1. IMPORTAR PILOTOS

app = FastAPI(
    title="RA KartRacing API",
    description="API para gestão financeira da equipe de kart RA KartRacing.",
    version="0.1.0"
)

app.include_router(categorias.router)
app.include_router(pilotos.router) # <-- 2. INCLUIR O ROUTER DE PILOTOS

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Bem-vindo à API da RA KartRacing!"}