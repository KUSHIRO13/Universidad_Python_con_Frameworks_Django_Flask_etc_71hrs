# Crear clase de Cubo
class Cubo:
    def __init__(self, base, altura, profundo):
        self.base = base
        self.altura = altura
        self.profundo = profundo

    def calcular_volumen(self):
        return (self.base * self.altura) * self.profundo


# Entrada de datos
ancho = int(input("Proporcione el ancho: "))
alto = int(input("Proporcione el alto: "))
profundidad = int(input("Proporcione la profundidad: "))

cubo = Cubo(ancho, alto, profundidad)
print(f"El volumen total del cubo es: {cubo.calcular_volumen()}")
