from datetime import datetime

def calculate_likelihood(breaches: list) -> float:
    """
    Calculates likelihood score (0.0 - 1.0) deterministically.
    
    Factors:
    - Recency: Newer breaches > Older breaches
    - Data Sensitivity: Passwords > PII > Metadata
    - Volume: saturation effect
    """
    if not breaches:
        return 0.05 # Baseline background radiation
    
    score = 0.0
    current_year = datetime.now().year
    
    for breach in breaches:
        # 1. Base Severity by Data Class
        breach_severity = 0.1
        data_classes = breach.get("data", [])
        
        if "Password" in data_classes:
            breach_severity = 0.8
        elif "Hash" in data_classes:
            breach_severity = 0.5
        elif "Phone" in data_classes:
            breach_severity = 0.4
            
        # 2. Recency Decay (Linear decay implementation for stability)
        # Assume breach input has 'date' or we default to '2020'
        breach_year = int(breach.get("date", "2020")[:4])
        years_ago = max(0, current_year - breach_year)
        
        # Decay factor: 0.9^years_ago
        time_weight = pow(0.9, years_ago)
        
        # Contribution
        score += (breach_severity * time_weight)
    
    # Sigmoid-like cap to 1.0, but simple min for deterministic clarity
    return min(score, 1.0)
