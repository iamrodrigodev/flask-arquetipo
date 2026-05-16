from abc import ABC, abstractmethod

class IAutenticacionService(ABC):
    @abstractmethod
    def registrar_cuenta(self, datos):
        pass

    @abstractmethod
    def iniciar_sesion(self, datos):
        pass

    @abstractmethod
    def obtener_sesion(self, usuario):
        pass
