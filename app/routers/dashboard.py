from fastapi import APIRouter, HTTPException
from app.schemas.dashboard import DashboardSummary
from app.db import crud_dashboard

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/summary", response_model=DashboardSummary)
def get_summary():
    summary_data = crud_dashboard.get_dashboard_summary()
    if summary_data is None:
        raise HTTPException(status_code=500, detail="Erro ao calcular o resummo do dashboard")
    return summary_data  