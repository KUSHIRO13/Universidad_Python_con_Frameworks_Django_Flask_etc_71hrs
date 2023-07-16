class Person:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Decoradores
    #   Get
    @property
    def nombre(self):
        print("Entro al get")
        return self._nombre

    #   Set
    @nombre.setter
    def nombre(self, name):
        print("Entro al set")
        self._nombre = name

usuario1 = Person("Kushiro","Amigama",25)
usuario1.nombre = "Andres"
print(usuario1.nombre)
