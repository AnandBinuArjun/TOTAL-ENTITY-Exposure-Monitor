from fastapi import APIRouter

router = APIRouter()

@router.get("/{identifier_id}")
async def get_actions(identifier_id: str):
    return {"id": identifier_id, "actions": []}
