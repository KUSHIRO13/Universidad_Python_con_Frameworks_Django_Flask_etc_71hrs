class Persona:
    contador_persona = 0
    def __init__(self, nombre, edad):
        Persona.contador_persona += 1
        self.id_persona = Persona.contador_persona
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f"Persona: {self.id_persona} {self._nombre} {self._edad}"

    # Decoradores
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad



persona = Persona("Andres", 19)
print(persona)

persona15 = Persona("Karla", 25)
print(persona15)

persona2 = Persona("Eduardo", 43)
print(persona2)

print(Persona.contador_persona)