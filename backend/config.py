import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    HIBP_API_KEY = os.getenv("HIBP_API_KEY", "")
    
settings = Settings()
