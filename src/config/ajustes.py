import os
from datetime import timedelta

class Ajustes:
    CLAVE_SECRETA = os.getenv('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_CLAVE_SECRETA = os.getenv('JWT_SECRET_KEY')
    JWT_ALGORITMO = os.getenv('JWT_ALGORITHM')
    
    _horas_expiracion = int(os.getenv('JWT_EXPIRATION_HOURS'))
    JWT_EXPIRACION_TOKEN = timedelta(hours=_horas_expiracion)
