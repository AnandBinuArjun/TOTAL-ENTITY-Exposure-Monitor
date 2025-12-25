def calculate_impact(service_type: str, blast_radius_multiplier: float = 1.0) -> float:
    """
    Calculates impact score (0.0 - 1.0) based on service criticality and its connectivity.
    
    Factors:
    - Service Tier: Financial/Infra > Social > Ent
    - Downstream Risk: Higher if it unlocks other accounts (blast radius)
    """
    impact_map = {
        "infrastructure": 1.0,  # Email, ISP, Phone - The Root
        "financial": 0.9,       # Banks, Paypal
        "cloud": 0.8,           # AWS, GCloud, Dropbox
        "government": 0.7,      # GovID, Taxes
        "medical": 0.6,
        "social": 0.5,          # High reputation damage
        "commerce": 0.4,
        "entertainment": 0.2,
        "forum": 0.1
    }
    
    base_impact = impact_map.get(service_type, 0.3)
    
    # Blast radius amplifier: If this node connects to many others, boost impact
    # Cap at 1.0
    final_impact = min(base_impact * blast_radius_multiplier, 1.0)
    
    return final_impact
