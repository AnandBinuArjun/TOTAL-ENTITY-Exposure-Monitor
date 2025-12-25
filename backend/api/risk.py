from fastapi import APIRouter

router = APIRouter()

@router.get("/{identifier_id}")
async def get_risk_score(identifier_id: str):
    return {"id": identifier_id, "score": 0, "breakdown": {}}
