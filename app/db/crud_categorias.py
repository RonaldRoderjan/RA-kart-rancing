# app/db/crud_categorias.py
from app.db.database import supabase_client

def get_all_categorias(): # <-- Verifique se o nome está exatamente assim
    try:
        # Garanta que o nome da tabela aqui também está em minúsculo
        response = supabase_client.from_("categorias").select("*").execute()
        return response.data
    except Exception as e:
        print(f"Ocorreu um erro ao buscar categorias: {e}")
        return None