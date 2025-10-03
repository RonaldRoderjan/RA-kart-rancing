from app.db.database import supabase_client
from app.schemas.transacao import TransacaoCreate

def create_transacao(db, transacao: TransacaoCreate):
    #Cria uma nova transação para um piloto.
    try:
        transacao_dict = transacao.model_dump()
        transacao_dict['tipo'] = transacao_dict['tipo'].value

        response = supabase_client.from_("transacoes").insert(transacao_dict).insert(transacao_dict).execute()

        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Ocorreu um erro ao criar a transação: {e}")
        return None
    
def get_transacoes_bypiloto(piloto_id: int):
    #Busca todas as transações de um piloto específico.
    try:
        response = supabase_client.from_("transacoes").select("*").eq("piloto_id",piloto_id).execute()
        return response.data
    except Exception as e:
        print(f"Ocorreu um erro ao buscar as transações do piloto: {e}")
        return None