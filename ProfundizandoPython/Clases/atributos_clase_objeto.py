class Persona:
    contador_persona = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        Persona.contador_persona += 1


# Mostrara atributos

persona1 = Persona('Juan', 'Perez')
print(persona1.__dict__) # Despliega los atributos del objeto

print(persona1.contador_persona)
# persona1.contador_persona = 10
# print(persona1.__dict__) # Despliega los atributos del objeto
print(Persona.contador_persona)
# print(persona1.contador_persona)

persona2 = Persona('Carlos', 'Cortina')
print(Persona.contador_persona)