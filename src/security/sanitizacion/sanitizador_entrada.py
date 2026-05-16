import bleach
import re

class SanitizadorDeEntrada:
    _PATRON_CONTROLES = re.compile(r"[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]")
    _PATRON_TAG_HTML = re.compile(r"<\s*/?\s*[a-zA-Z][^>]*>")

    @staticmethod
    def sanitizar(entrada):
        if not isinstance(entrada, str):
            return entrada
        
        valor = SanitizadorDeEntrada._PATRON_CONTROLES.sub("", entrada)
        valor = valor.strip()

        if not valor:
            return valor

        if SanitizadorDeEntrada._PATRON_TAG_HTML.search(valor):
            valor = bleach.clean(valor, tags=[], attributes={}, strip=True)

        return valor
