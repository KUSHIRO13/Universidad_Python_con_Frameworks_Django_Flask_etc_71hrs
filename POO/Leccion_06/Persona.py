class Persona:
    contador_persona = 0
    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_valor()
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f"Persona: {self.id_persona} {self._nombre} {self._edad}"

    @classmethod
    def _generar_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona

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

persona2 = Persona("Karla", 25)
print(persona2)

persona3 = Persona("Eduardo", 43)
print(persona3)

# Persona.generar_valor()

persona4 = Persona("Luis", 15)
print(persona4)

print(Persona.contador_persona)