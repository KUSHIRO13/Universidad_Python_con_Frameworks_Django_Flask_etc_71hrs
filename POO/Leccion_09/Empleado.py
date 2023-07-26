class Empleado:
    def __init__(self, nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo

    def __str__(self):
        return f"Empleado: {self._nombre}\nSueldo: {self._sueldo}"

    def mostrar_detalles(self):
        return self.__str__()

    @property
    def nombre(self):
        return self._nombre

    @property
    def sueldo(self):
        return self._sueldo

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
