from typing import List, Dict

class ServiceNode:
    def __init__(self, name: str, category: str, url: str):
        self.name = name
        self.category = category  # e.g., Banking, Social, Email
        self.url = url
        self.connected_nodes = []

    def connect(self, node):
        self.connected_nodes.append(node)

class IdentityMap:
    def __init__(self):
        self.graph = {}

    def build_graph(self, identifier: str) -> Dict:
        """
        Builds a graph of services associated with the identifier.
        This represents the 'Blast Radius'.
        
        Returns a dict suitable for React Flow or D3 visualization.
        """
        # In a real build, we would query the database for known accounts linked to this identifier.
        # Here we simulate a "Standard Consumer Profile"
        
        nodes = []
        edges = []
        
        # Root
        nodes.append({"id": "root", "label": identifier, "type": "identity"})
        
        # Tier 1: Infrastructure (High Impact)
        nodes.append({"id": "email_1", "label": "Gmail Primary", "type": "infrastructure"})
        edges.append({"source": "root", "target": "email_1", "label": "owns"})
        
        # Tier 2: Financial (High Impact)
        nodes.append({"id": "bank_1", "label": "Chase", "type": "financial"})
        nodes.append({"id": "paypal", "label": "PayPal", "type": "financial"})
        
        # Edges showing Recovery Authority
        edges.append({"source": "email_1", "target": "bank_1", "label": "recovery_authority"}) 
        edges.append({"source": "email_1", "target": "paypal", "label": "recovery_authority"})
        
        # Tier 3: Social/Cloud (Medium Impact)
        nodes.append({"id": "dropbox", "label": "Dropbox", "type": "cloud"})
        nodes.append({"id": "fb", "label": "Facebook", "type": "social"})
        
        edges.append({"source": "email_1", "target": "dropbox", "label": "recovery_authority"})
        edges.append({"source": "email_1", "target": "fb", "label": "recovery_authority"})
        
        # Tier 4: Risky Fanout (SSO)
        # If Facebook is compromised, Spotify and Tinder are exposed via SSO
        nodes.append({"id": "spotify", "label": "Spotify", "type": "entertainment"})
        nodes.append({"id": "tinder", "label": "Tinder", "type": "social"})
        
        edges.append({"source": "fb", "target": "spotify", "label": "sso_provider"})
        edges.append({"source": "fb", "target": "tinder", "label": "sso_provider"})

        return {
            "nodes": nodes,
            "edges": edges
        }
