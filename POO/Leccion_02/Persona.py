class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Decorador
    @property
    def nombres(self):
        print("Llamado get nombre")
        return self._nombre

    @nombres.setter
    def nombres(self, nombre):
        print("Llamado set nombre")
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self.apellido} {self.edad}")


persona1 = Persona("Andres", "Cortina", 19)
print(persona1.nombres)

persona1.nombres = "Kushiro"
print(persona1.nombres)
