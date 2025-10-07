# app/routers/auth.py
from fastapi import APIRouter, HTTPException, status
from app.db.database import supabase_client
from app.schemas.auth import UserLogin, Token

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)

@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin):
    try:
        response = supabase_client.auth.sign_in_with_password({
            "email": user_credentials.email,
            "password": user_credentials.password
        })

        access_token = response.session.access_token
        if not access_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token não encontrado.")

        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos.",
            headers={"WWW-Authenticate": "Bearer"},
        )