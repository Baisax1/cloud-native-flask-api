from dotenv import load_dotenv
import os

load_dotenv()



class Config:
    """Configuración base de los entornos"""
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    
class DevConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    
class TestConfig(Config):
    """Configuración para pruebas"""
    TESTING = True
    DEBUG = True
    
class ProdConfig(Config):
    """Configuración de Producción  """
    DEBUG = False
    
    
    
    
config_by_name = {
    "development": DevConfig,
    "testing": TestConfig,
    "production": ProdConfig,
    "default": DevConfig
}