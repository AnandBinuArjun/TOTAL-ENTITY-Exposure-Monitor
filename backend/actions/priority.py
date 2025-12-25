from typing import List, Dict

EFFORT_SCORES = {
    "change_password": 3,   # 1-10 scale
    "enable_2fa": 4,
    "hardware_key": 8,
    "review_activity": 2
}

def prioritize_actions(risks: List[Dict]) -> List[Dict]:
    """
    Rank actions by (Risk Reduction / User Effort).
    """
    action_plan = []
    
    for risk in risks:
        current_risk_score = risk["score"]
        service = risk["service"]
        
        # Hypothetical Actions
        potential_actions = [
            {"type": "change_password", "reduction": 0.4},
            {"type": "enable_2fa", "reduction": 0.7}
        ]
        
        for action in potential_actions:
            reduction_value = current_risk_score * action["reduction"]
            effort = EFFORT_SCORES.get(action["type"], 5)
            
            priority_score = reduction_value / effort
            
            action_plan.append({
                "service": service,
                "action": action["type"],
                "priority_score": round(priority_score, 2),
                "reason": f"Reduces risk by {int(action['reduction']*100)}% with effort level {effort}"
            })
            
    # Sort by priority desc
    return sorted(action_plan, key=lambda x: x["priority_score"], reverse=True)
