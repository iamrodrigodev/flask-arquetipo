import jwt
from datetime import datetime
from flask import current_app

class ServicioJwt:
    @staticmethod
    def generar_token(usuario_id):
        payload = {
            'sub': usuario_id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + current_app.config['JWT_EXPIRACION_TOKEN']
        }
        return jwt.encode(
            payload,
            current_app.config['JWT_CLAVE_SECRETA'],
            algorithm=current_app.config['JWT_ALGORITMO']
        )

    @staticmethod
    def decodificar_token(token):
        try:
            payload = jwt.decode(
                token,
                current_app.config['JWT_CLAVE_SECRETA'],
                algorithms=[current_app.config['JWT_ALGORITMO']]
            )
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
        except Exception:
            return None
