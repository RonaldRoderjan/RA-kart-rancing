# app/db/crud_pilotos.py
from app.db.database import supabase_client
from app.schemas.piloto import PilotoCreate

def get_all_pilotos():
    try:
        response_pilotos = supabase_client.from_("pilotos").select("*").execute()
        if not response_pilotos.data:
            return []
        
        response_categorias = supabase_client.from_("categorias").select("*").execute()
        if not response_categorias.data:
            return response_pilotos.data

        categorias_map = {cat['categoria_id']: cat for cat in response_categorias.data}

        pilotos_com_categoria = []
        for piloto in response_pilotos.data:
            categoria_id = piloto.get("categoria_id")
            if categoria_id in categorias_map:
                piloto['categoria'] = categorias_map[categoria_id]
            else:
                piloto['categoria'] = None
            pilotos_com_categoria.append(piloto)
        
        return pilotos_com_categoria
    except Exception as e:
        print(f"Ocorreu um erro ao buscar os pilotos (junção manual): {e}")
        return None

def create_piloto(piloto: PilotoCreate):
    try:
        piloto_dict = piloto.model_dump()
        response = supabase_client.from_("pilotos").insert(piloto_dict).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Ocorreu um erro ao criar o piloto: {e}")
        return None