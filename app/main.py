# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import categorias, pilotos, transacoes, dashboard

app = FastAPI(
    title="RA KartRacing API",
    description="API para gestão financeira da equipe de kart RA KartRacing.",
    version="0.1.0"
)

# Define os endereços que podem acessar a API
origins = [
    "http://localhost:5173",
]

# Adiciona a configuração de CORS ao FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra os endpoints
app.include_router(categorias.router)
app.include_router(pilotos.router)
app.include_router(transacoes.router)
app.include_router(dashboard.router)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Bem-vindo à API da RA KartRacing!"}