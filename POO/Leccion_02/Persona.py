class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # Decorador
    @property
    def nombres(self):
        print("Llamado get nombre")
        return self._nombre

    @nombres.setter
    def nombres(self, nombre):
        print("Llamado set nombre")
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self._apellido} {self._edad}")

    def __del__(self):
        print(f"Eliminacion de {self._nombre} {self._apellido} exitosa")



if __name__ == "__main__":
    persona1 = Persona("Andres", "Cortina", 19)
    print(persona1.nombres)

    persona1.nombres = "Kushiro"
    print(persona1.nombres)
    print(persona1.apellido)
    print(persona1.edad)
    print(__name__)
    print(__name__)