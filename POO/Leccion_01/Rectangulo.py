# Crear clase Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


print("Bienvenido al primer programa con POO en donde se calculara el area de un rectangulo")
base = int(input("Por favor, ingrese la base: "))
altura = int(input("Por favor, ingrese la altua: "))

# llamado de clase
rectangulo = Rectangulo(base, altura)
print(f"El area total es: {rectangulo.calcular_area()}")
