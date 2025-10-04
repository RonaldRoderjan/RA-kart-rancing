# app/db/crud_pilotos.py
from app.db.database import supabase_client
from app.schemas.piloto import PilotoCreate, PilotoUpdate
from datatime import date

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

def get_piloto_summary(piloto_id):
    try:
        response_piloto = supabase_client.from_("pilotos").select("valor_mensalidade").eq("piloto_id", piloto_id).single().execute()
        if not response_piloto.data:
            return None
        
        mensalidade = response_piloto.data.get('valor_mensalidade', 0)

        today = date.today()
        start_of_month = today.replace(day=1)

        response_transacoes = supabase_client.from_("transacoes").select("valor, tipo").eq("piloto_id", piloto_id).gte("data_transacao", str(start_of_month)).execute()
     
        total_gastos = 0.0
        total_reembolso = 0.0
        if response_transacoes.data:
            for transacao in response_transacoes.data:
                if transacao['tipo'] == 'GASTO_EXTRA':
                    total_gasto += transacao['valor']
                elif transacao['tipo'] == 'REEMBOLSO':
                    total_reembolsos += transacao['valor']
    
            valor_final = mensalidade + total_gastos - total_reembolsos

            summary = {
            "valor_mensalidade": mensalidade,
            "total_gastos_extras": total_gastos,
            "total_reembolsos": total_reembolsos,
            "valor_final_mes": valor_final
            }
            return summary

    except Exception as e:
        print(f"Ocorreu um erro ao calcular o resumo do piloto: {e}")
        return