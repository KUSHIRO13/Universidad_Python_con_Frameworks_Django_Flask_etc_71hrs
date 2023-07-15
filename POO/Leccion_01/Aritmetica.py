class Aritmetica:
    """
    Clase Aritmetica para la realizacion de operaciones de
    Suma
    Resta
    etc
    """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        suma = self.num1 + self.num2
        return f"La suma de {self.num1} y {self.num2} es: {suma}"

    def resta(self):
        resta = self.num1 - self.num2
        return f"La resta de {self.num1} y {self.num2} es: {resta}"

    def multiplicar(self):
        multiplicar = self.num1 * self.num2
        return f"La multiplicacion de {self.num1} y {self.num2} es: {multiplicar}"

    def division(self):
        division = self.num2 / self.num1
        return f"La division entre {self.num2} y {self.num1} es: {division:.2f}"


matematicas = Aritmetica(5, 3)

# Resultados
print(matematicas.suma())
print(matematicas.resta())
print(matematicas.multiplicar())
print(matematicas.division())
