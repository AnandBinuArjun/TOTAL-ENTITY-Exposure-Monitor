import httpx
import logging
from typing import List, Dict
from backend.config import settings

logger = logging.getLogger(__name__)

async def check_hibp_breaches(identifier: str) -> List[Dict]:
    """
    Queries Have I Been Pwned API v3 for breaches associated with an email.
    Requires HIBP_API_KEY in .env.
    """
    if not settings.HIBP_API_KEY:
        logger.warning("No HIBP_API_KEY found. Identifying as mock mode.")
        # Fallback to internal mock if no key
        return []

    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{identifier}?truncateResponse=false"
    headers = {
        "hibp-api-key": settings.HIBP_API_KEY,
        "user-agent": "Total-Entity-Monitor"
    }

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, headers=headers, timeout=10.0)
            
            if resp.status_code == 200:
                data = resp.json()
                # Normalize to our internal format
                normalized = []
                for item in data:
                    normalized.append({
                        "source": item.get("Name"),
                        "domain": item.get("Domain"),
                        "date": item.get("BreachDate"),
                        "data": item.get("DataClasses", []),
                        "description": item.get("Description")
                    })
                return normalized
                
            elif resp.status_code == 404:
                return [] # No breaches found
                
            elif resp.status_code == 429:
                logger.error("HIBP Rate Limit Exceeded")
                return []
                
    except Exception as e:
        logger.error(f"HIBP API Error: {e}")
        return []

    return []
