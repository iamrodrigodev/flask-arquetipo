from pydantic import BaseModel, Field, field_validator
from pydantic_core import PydanticCustomError
import re
from src.security.sanitizacion.sanitizador_entrada import SanitizadorDeEntrada

class RegistroPeticion(BaseModel):
    nombre: str = Field(...)
    apellidos: str = Field(...)
    correo: str = Field(...)
    clave: str = Field(...)
    
    telefono: str = Field(None)
    direccion: str = Field(None)
    referencia: str = Field(None)
    codigo_postal: str = Field(None)
    distrito_id: str = Field(None)

    @field_validator('nombre', 'apellidos', 'direccion', 'referencia', 'codigo_postal', mode='before')
    @classmethod
    def sanitizar_campos_texto(cls, v):
        if isinstance(v, str):
            return SanitizadorDeEntrada.sanitizar(v)
        return v

    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, v):
        if not v or len(v.strip()) == 0:
            raise PydanticCustomError('value_error', 'El nombre es obligatorio')
        return v

    @field_validator('apellidos')
    @classmethod
    def validar_apellidos(cls, v):
        if not v or len(v.strip()) == 0:
            raise PydanticCustomError('value_error', 'Los apellidos son obligatorios')
        return v

    @field_validator('correo')
    @classmethod
    def validar_correo(cls, v):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not v or not re.match(regex, v):
            raise PydanticCustomError('value_error', 'El formato del correo electrónico no es válido')
        return v

    @field_validator('clave')
    @classmethod
    def validar_clave(cls, v):
        if not v or len(v) < 6:
            raise PydanticCustomError('value_error', 'La clave debe tener al menos 6 caracteres')
        return v
