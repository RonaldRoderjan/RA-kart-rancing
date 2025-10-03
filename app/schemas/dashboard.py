from pydantic import BaseModel

class DashboardSummary(BaseModel):
    total_pilotos_ativos: int
    receita_mensal_prevista: float
    gastos_extras_mes: float
    total_geral_mes: float

