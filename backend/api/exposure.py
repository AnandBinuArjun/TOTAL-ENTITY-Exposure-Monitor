from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class IdentifierInput(BaseModel):
    value: str
    type: str  # email, phone, username, domain
    privacy_mode: Optional[bool] = True

@router.post("/check", response_model=None) # We can use schemas.RiskReport here if we imported it
async def check_exposure(identifier: IdentifierInput):
    # 1. Privacy
    from backend.privacy import hashing
    prefix = hashing.get_k_anonymity_prefix(identifier.value)
    
    # 2. Ingestion (Hybrid: Real + Fallback)
    from backend.ingestion import breaches, live_breaches
    
    # Try live fetch first
    breach_hits = await live_breaches.check_hibp_breaches(identifier.value)
    
    # If live returned nothing (either clean or no key), and we want to demo:
    # In a real PROD app, we wouldn't show mock data if there's no key, 
    # but for this "Cortex" demo to work without a paid key, we might keep mock fallback 
    # OR strictly return empty. 
    # Implementation decision: If no key is set, show Mock. If key set, show Real.
    from backend.config import settings
    if not settings.HIBP_API_KEY and not breach_hits:
         breach_hits = breaches.check_breaches(prefix)
    
    # 3. Identity Graph
    from backend.graph import identity_map
    mapper = identity_map.IdentityMap()
    graph_data = mapper.build_graph(identifier.value)
    
    # 4. Risk Calculation
    from backend.scoring import likelihood, impact, mitigation
    
    calculated_node_risks = []
    total_score = 0
    
    # Build a lookup for edges to calculate blast radius factor
    # For now, simplistic: how many outbound edges does a node have?
    outbound_counts = {}
    for edge in graph_data["edges"]:
        src = edge["source"]
        outbound_counts[src] = outbound_counts.get(src, 0) + 1

    for node in graph_data["nodes"]:
        if node["id"] == "root": continue
        
        # Determine specific attributes
        is_breached_service = any(b.get("source", "").lower() in node["label"].lower() for b in breach_hits)
        
        # Likelihood:
        # If the specific service is breached, L is high.
        # If the root email is breached, L is moderate for connected services (credential stuffing risk).
        if is_breached_service:
             l_score = 0.9
        else:
             # Inherited risk from base email breach
             l_score = likelihood.calculate_likelihood(breach_hits)

        # Impact:
        # Multiplier depends on how many things this node unlocks
        fanout = outbound_counts.get(node["id"], 0)
        blast_multiplier = 1.0 + (fanout * 0.2)
        
        i_score = impact.calculate_impact(node["type"], blast_radius_multiplier=blast_multiplier)
        
        # Mitigation:
        # Mocking: Check if user has protections (normally from DB)
        current_protections = [] 
        # Simulation: If it's a bank, maybe they have SMS 2FA
        if node["type"] == "financial":
            current_protections.append("2fa_sms")
            
        m_score = mitigation.calculate_mitigation(current_protections) 
        
        # Final Node Risk Formula: R = L * I * (1 - M)
        # Scaled to 0-100
        node_risk_raw = (l_score * i_score) * (1.0 - m_score)
        node_risk = node_risk_raw * 100.0
        
        calculated_node_risks.append({
            "service": node["label"],
            "score": node_risk,
            "details": {"L": l_score, "I": i_score, "M": m_score}
        })
        
        # Aggregate logic (e.g. max or root-mean-square)
        # Here we take the max risk item as the defining score for the user
        if node_risk > total_score:
            total_score = node_risk

    # 5. Action Prioritization
    from backend.actions import priority
    plan = priority.prioritize_actions(calculated_node_risks)

    return {
        "status": "complete",
        "identifier_masked": prefix + "***",
        "breach_count": len(breach_hits),
        "risk_score": min(total_score, 100), 
        "graph": graph_data,
        "actions": plan
    }

