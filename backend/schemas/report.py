from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

class RiskComponent(BaseModel):
    likelihood: float = Field(..., description="0.0 to 1.0 score of breach probability")
    impact: float = Field(..., description="0.0 to 1.0 score of potential damage")
    mitigation: float = Field(..., description="0.0 to 1.0 score of existing protections")
    final_score: float = Field(..., description="calculated risk score 0-100")

class IdentityNode(BaseModel):
    id: str
    label: str
    type: str  # service, email, device
    criticality: float
    risk_component: Optional[RiskComponent] = None

class ActionItem(BaseModel):
    id: str
    service_id: str
    action_type: str
    description: str
    priority_score: float = Field(..., description="ROI: Risk Reduction / Effort")
    effort_score: int = Field(..., description="1-10 scale")
    risk_reduction: float = Field(..., description="Absolute risk point reduction")

class RiskReport(BaseModel):
    report_id: str
    generated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Context
    identifier_masked: str
    
    # Intelligence
    breach_count: int
    data_sources: List[str]
    
    # Core Risk
    total_risk_score: float
    risk_level: str  # LOW, MEDIUM, CRITICAL
    
    # Graph
    nodes: List[IdentityNode]
    edges: List[Dict[str, str]]
    
    # Remediation
    action_plan: List[ActionItem]
