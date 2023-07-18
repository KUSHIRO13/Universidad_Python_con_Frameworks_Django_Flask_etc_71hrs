class MiClase:
    variable_clase = "Variable de Clase"
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)

miclase = MiClase("Hola")

print(miclase.variable_instancia)
print(miclase.variable_clase)
miclase.variable_instancia = "Hola como estas"

print(miclase.variable_instancia)
# Al vuelo
MiClase.variable_clase2 = "Variable dos"
print(miclase.variable_clase2)