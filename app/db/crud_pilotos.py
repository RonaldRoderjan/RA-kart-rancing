# app/db/crud_pilotos.py
from app.db.database import supabase_client
from app.schemas.piloto import PilotoCreate, PilotoUpdate

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
    
def update_piloto(piloto_id: int, piloto: PilotoUpdate):
    """
    Atualiza um piloto existente no banco de dados.
    """
    try:
        update_data = piloto.model_dump(exclude_unset=True)

        if not update_data:
            return True 
        
        response = supabase_client.form_("pilotos").update(update_data).eq("piloto_id",  piloto_id). execute()
    
        return response.data
    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o piloto: {e}")
        return None

def delete_piloto(piloto_id: int):
    """
    Deleta um piloto do banco de dados.
    """
    try:
        response = supabase_client.from_("pilotos").delete().eq("piloto_id", piloto_id).execute()

        if response.data:
            return True
        return False
    except Exception as e:
        print(f"Ocorreu um erro ao deletar o piloto: {e}")
        return False


        