from typing import List, Dict

# Mock Database of Breaches
MOCK_BREACHES = {
    "linkedin": {"name": "LinkedIn", "date": "2012-06-05", "data_classes": ["Password", "Email"]},
    "adobe": {"name": "Adobe", "date": "2013-10-04", "data_classes": ["Password", "Email", "Username", "Hint"]},
    "canva": {"name": "Canva", "date": "2019-05-24", "data_classes": ["Password", "Email", "Name", "City"]}
}

def check_breaches(identifier_hash_prefix: str) -> List[Dict]:
    """
    Simulates checking a breach database using k-anonymity prefix.
    In a real system, this would query a large DB or API.
    """
    # For demo purposes, return a static list if the prefix matches "something"
    # or just return random results for testing.
    return [
        {"source": "LinkedIn", "risk_score": 8, "data": ["Email", "Password"]},
        {"source": "Adobe", "risk_score": 6, "data": ["Email", "Password", "Hint"]}
    ]
