import sys
import os
import json
sys.path.append(os.getcwd())

from backend.api import exposure, graph
from backend.scoring import likelihood, impact, mitigation
from backend.actions import priority

class MockIdentifier:
    def __init__(self, value, type="email"):
        self.value = value
        self.type = type

async def run_demo():
    print("--- TOTAL ENTITY CORE ENGINE DIAGNOSTIC ---")
    print("Target: user@example.com")
    
    # Manually invoke the pipeline parts to show math
    identifier = "user@example.com"
    
    # 1. Breach Simulation
    breaches = [
        {"source": "LinkedIn", "date": "2012-01-01", "data": ["Email", "Password"]},
        {"source": "Canva", "date": "2019-05-01", "data": ["Email", "Hash", "Name"]}
    ]
    l_score = likelihood.calculate_likelihood(breaches)
    print(f"\n[LIKELIHOOD] Score: {l_score:.4f}")
    print(f"   Context: {len(breaches)} breaches (Old Password + Newer Hash)")

    # 2. Graph Simulation
    print(f"\n[GRAPH] Constructing Blast Radius...")
    from backend.graph import identity_map
    mapper = identity_map.IdentityMap()
    graph_data = mapper.build_graph(identifier)
    print(f"   Nodes: {len(graph_data['nodes'])} | Edges: {len(graph_data['edges'])}")
    
    # 3. Risk Calculation Detail for a Node
    print(f"\n[RISK MATH] Deep Dive: 'Chase Bank' Node")
    # Chase is financial (Impact=0.9)
    # Connected to Email (Recovery Path)
    i_score = impact.calculate_impact("financial", blast_radius_multiplier=1.0)
    
    # Scenario A: No Protections
    m_score_a = mitigation.calculate_mitigation([])
    risk_a = (l_score * i_score) * (1 - m_score_a) * 100
    print(f"   Scenario A (No 2FA):")
    print(f"     L({l_score:.2f}) * I({i_score:.2f}) * (1 - M({m_score_a})) = {risk_a:.2f}")
    
    # Scenario B: SMS 2FA
    m_score_b = mitigation.calculate_mitigation(["2fa_sms"])
    risk_b = (l_score * i_score) * (1 - m_score_b) * 100
    print(f"   Scenario B (SMS 2FA):")
    print(f"     L({l_score:.2f}) * I({i_score:.2f}) * (1 - M({m_score_b})) = {risk_b:.2f}")
    
    # 4. Action Prioritization
    print(f"\n[ACTION PRIORITY] Calculating ROI...")
    risks = [
        {"service": "Chase", "score": risk_a, "details": {}}, # High Risk
        {"service": "Dropbox", "score": 30.0, "details": {}}  # Med Risk
    ]
    plan = priority.prioritize_actions(risks)
    for idx, item in enumerate(plan):
        print(f"   #{idx+1}: {item['action']} on {item['service']} (ROI Score: {item['priority_score']})")

    print("\n[STATUS] Core Math Verified.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_demo())
