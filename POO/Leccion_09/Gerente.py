from Empleado import Empleado
class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self._departamento = departamento

    def __str__(self):
        return f"Gerente: {self._departamento}\n{super().__str__()}"

    @property
    def departamento(self):
        return self._departamento
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento