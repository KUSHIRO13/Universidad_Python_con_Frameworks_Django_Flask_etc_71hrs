class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return self.nombre + other.nombre

    def __sub__(self, other):
        return self.edad - other.edad
