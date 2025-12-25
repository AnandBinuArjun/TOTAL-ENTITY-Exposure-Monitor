from fastapi import FastAPI
from backend.api import exposure, graph, risk, actions, enterprise

app = FastAPI(
    title="TOTAL ENTITY Exposure Monitor",
    description="Identity Risk Intelligence System",
    version="1.0.0"
)

# Include routers
app.include_router(exposure.router, prefix="/api/v1/exposure", tags=["Exposure"])
app.include_router(graph.router, prefix="/api/v1/graph", tags=["Identity Graph"])
app.include_router(risk.router, prefix="/api/v1/risk", tags=["Risk Scoring"])
app.include_router(actions.router, prefix="/api/v1/actions", tags=["Actions"])
app.include_router(enterprise.router, prefix="/api/v1/enterprise", tags=["Enterprise"])

@app.get("/")
def read_root():
    return {"system": "TOTAL ENTITY Exposure Monitor", "status": "active"}
