class Persona(object):
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f"Persona: \nNombre: {self._nombre}\nEdad: {self._edad}"

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f"{super().__str__()}\nSueldo: {self.sueldo}"


if __name__ == "__main__":
    empleado1 = Empleado("Andres", 19, 50000)
    print(empleado1.sueldo)
    print(empleado1.nombre)
    empleado1.nombre = "Kushiro"
    print(empleado1.nombre)