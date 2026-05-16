import random
import string

class GeneradorCodigoUtil:
    @staticmethod
    def generar_codigo_seis_digitos():
        return ''.join(random.choices(string.digits, k=6))
