class PersonaCopy:
    def __init__(self,nombre, apellido, edad):
        self.nombres = nombre
        self.apellidos = apellido
        self.edades = edad
    # def __str__(self):
    #     pass
    #
    # def __repr__(self):
    #     pass

persona1 = PersonaCopy("Andres", "Cortina", 19)
print(f"Objeto Persona 1: {persona1.nombres} {persona1.apellidos} {persona1.edades}")

persona1.nombres = "Kushiro"
persona1.apellidos = "Amigama"
persona1.edades = 25
print(f"Objeto Persona 1: {persona1.nombres} {persona1.apellidos} {persona1.edades}")

persona2 = PersonaCopy("Daniela", "Gutierres", 17)
print(f"Objeto Persona 2: {persona2.nombres} {persona2.apellidos} {persona2.edades}")

edad = 25
persona2.nombres = 255
persona2.apellidos = "Adobe"
persona2.edades = edad

print(f"Objeto Persona 2: {persona2.nombres} {persona2.apellidos} {persona2.edades}")
