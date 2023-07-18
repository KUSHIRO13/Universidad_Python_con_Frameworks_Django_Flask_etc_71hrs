from FiguraGeometrica import *
from Color import *


class Rectangulo(FiguraGeometrica, Color, ):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def __str__(self):
        return f"Los valores proporcionados son: {FiguraGeometrica.__str__(self)} {Color.__str__(self)} " \
               f"{Rectangulo.calcular_area(self)}"

    def calcular_area(self):
        return f"\nArea: {self.alto * self.ancho}"


if __name__ == "__main__":
    rectangulo1 = Rectangulo(6, 6, "Azul")
    print(rectangulo1)
    rectangulo2 = Rectangulo(6, 9, "Negro")
    rectangulo3 = Rectangulo(8, 2, "Azul Cielo")
    rectangulo4 = Rectangulo(5, 4, "Purpura")

    print(rectangulo2)
    print(rectangulo3)
    print(rectangulo4)
