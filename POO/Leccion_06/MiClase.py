class MiClase:
    variable_clase = "Variable de Clase"
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    def dinamico(self):
        print("Metodo dinamico")
        self.metodo_clase()
        self.metodo_estatico()

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase, " Metodo Estatico")

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase, " Metodo de Clase")

"""
print(MiClase.variable_clase)

miclase = MiClase("Hola")

print(miclase.variable_instancia)
print(miclase.variable_clase)
miclase.variable_instancia = "Hola como estas"

print(miclase.variable_instancia)
# Al vuelo
MiClase.variable_clase2 = "Variable dos"
print(miclase.variable_clase2)
miclase.metodo_estatico()
MiClase.metodo_estatico()

# Metodo de clase
miclase.metodo_clase()
MiClase.metodo_clase()
"""

miObjecto1 = MiClase("Variable")
miObjecto1.metodo_clase()
miObjecto1.dinamico()