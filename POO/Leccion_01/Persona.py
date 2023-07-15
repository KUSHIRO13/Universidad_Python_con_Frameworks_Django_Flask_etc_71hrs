class Persona:
    def __init__(self,nombre, apellido, edad):
        self.nombres = nombre
        self.apellidos = apellido
        self.edades = edad

    def mostrar_detalles(self):
        print(f"Persona: {self.nombres} {self.apellidos} {self.edades}")

persona1 = Persona("Andres", "Cortina", 19)
persona1.mostrar_detalles()

persona2 = Persona("Daniela", "Gutierres", 17)
persona2.mostrar_detalles()

Persona.mostrar_detalles(persona1)

# Agregar atributo (Solo funciona en el objeto solo)
persona1.telefono = 3007429664
print(persona1.telefono)

# Agregar para el persona 2
persona2.correo = "danielagutierres@gmail.com"
print(persona2.correo)

