# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import categorias, pilotos, transacoes, dashboard, auth

app = FastAPI(
    title ="RA KartRacing API",
    description = "API para getão financeira da equipe de kart RA KartRacing.",
    version = "0.1.0"
)

# A lista de origens agora permite tudo
origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categorias.router)
app.include_router(pilotos.router)
app.include_router(transacoes.router)
app.include_router(dashboard.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Bem-vindo à API da RA KartRancing"}
