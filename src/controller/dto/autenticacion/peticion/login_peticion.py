from pydantic import BaseModel, EmailStr, Field

class LoginPeticion(BaseModel):
    correo: EmailStr = Field(..., max_length=150)
    clave: str = Field(..., min_length=6, max_length=255)
