from abc import ABC, abstractmethod

class IUsuarioService(ABC):
    @abstractmethod
    def obtener_perfil(self, usuario):
        pass
