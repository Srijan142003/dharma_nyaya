import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    API_KEY = os.getenv('API_KEY', '')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    
    # Add other configuration variables as needed
