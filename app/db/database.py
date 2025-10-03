# app/db/database.py
from supabase import create_client, Client
from app.core.config import settings

# Cria o cliente de conexão com o Supabase
supabase_client: Client = create_client(
    supabase_url=settings.SUPABASE_URL, 
    supabase_key=settings.SUPABASE_KEY
)