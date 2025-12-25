import hashlib

def hash_identifier(identifier: str) -> str:
    """Returns SHA-256 hash of the identifier."""
    return hashlib.sha256(identifier.encode()).hexdigest()

def get_k_anonymity_prefix(identifier: str, k: int = 5) -> str:
    """Returns the first k characters of the hash for k-anonymity lookup."""
    full_hash = hash_identifier(identifier)
    return full_hash[:k]
