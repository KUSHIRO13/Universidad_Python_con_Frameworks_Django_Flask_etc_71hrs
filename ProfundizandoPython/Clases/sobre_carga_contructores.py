# Simulacion de sobrecarga
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_valores(cls):
        return cls('Karla', 'Gomez')

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Apellido: {self.apellido}")



persona1 = Persona('Juan', 'Perez')
persona_vacio = Persona.crear_persona_vacia()
persona2 = Persona.crear_persona_valores()

print(persona1)
print(persona_vacio)
print(persona2)
