from app.db.database import supabase_client
from datetime import date

def get_dashboard_summary():
    try:
        # 1. Total de Pilotos Ativos
        response_pilotos = supabase_client.from_("pilotos").select("piloto_id, valor_mensalidade", count='exact').eq("ativo", True).execute()
        total_pilotos_ativos = response_pilotos.count if response_pilotos.count is not None else 0

        # 2. Receita Mensal Prevista
        receita_mensal_prevista = sum(piloto['valor_mensalidade'] for piloto in response_pilotos.data)

        # 3. Gastos Extras do Mês Corrente
        today = date.today()
        start_of_month = today.replace(day=1)
        
        response_gastos = supabase_client.from_("transacoes").select("valor").eq("tipo", "GASTO_EXTRA").gte("data_transacao", str(start_of_month)).execute()
        gastos_extras_mes = sum(gasto['valor'] for gasto in response_gastos.data)
        
        # 4. Cálculo do Total Geral
        total_geral_mes = receita_mensal_prevista + gastos_extras_mes

        summary = {
            "total_pilotos_ativos": total_pilotos_ativos,
            "receita_mensal_prevista": receita_mensal_prevista,
            "gastos_extras_mes": gastos_extras_mes,
            "total_geral_mes": total_geral_mes
        }
        return summary

    except Exception as e:
        print(f"Ocorreu um erro ao calcular o resumo do dashboard: {e}")
        return None