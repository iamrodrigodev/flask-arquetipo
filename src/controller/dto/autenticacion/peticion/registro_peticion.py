from pydantic import BaseModel, EmailStr, Field

class RegistroPeticion(BaseModel):
    nombre: str = Field(..., max_length=100)
    apellidos: str = Field(..., max_length=100)
    correo: EmailStr = Field(..., max_length=150)
    clave: str = Field(..., min_length=6, max_length=255)
    telefono: str = Field(None, max_length=12)
    direccion: str = Field(None, max_length=255)
    referencia: str = Field(None, max_length=255)
    codigo_postal: str = Field(None, max_length=10)
    distrito_id: str = Field(None, max_length=6)
