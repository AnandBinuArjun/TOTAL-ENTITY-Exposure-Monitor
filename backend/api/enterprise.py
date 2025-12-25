from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
async def get_enterprise_dashboard():
    return {"stats": {}, "alerts": []}
