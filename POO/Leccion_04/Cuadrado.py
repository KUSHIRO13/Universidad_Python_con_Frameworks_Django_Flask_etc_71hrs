from FiguraGeometrica import *
from Color import *


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self):
        return f"Los valores proporcioandos son:{FiguraGeometrica.__str__(self)} {Color.__str__(self)}" \
               f"{Cuadrado.calcular_area(self)}"

    def calcular_area(self):
        return f"\nArea: {self.alto * self.ancho}"
