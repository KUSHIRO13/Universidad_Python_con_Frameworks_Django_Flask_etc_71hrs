# ABC Abstract Basic Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Valor erroneo ancho: {self._ancho}")

        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0


    def __str__(self):
        return f"\nAlto: {self._alto}\nAncho: {self._ancho}"

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print("Valor erroneo")

    @abstractmethod
    def calcular_area(self):
        pass

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print("Valor erroneo")

    def _validar_valor(self, valor):
        return True if 0 < valor <= 20 else False