import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

class Config:
    DB_URL = os.getenv("DB_URL", "sqlite:///f1_drivers.db")
