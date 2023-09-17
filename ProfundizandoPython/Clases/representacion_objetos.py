# Representacion de objetos (str,repr, format)

# print(dir(object))
# help(object.__repr__)

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # repr, mas enfocado a los programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre: {self.nombre}, apellido: {self.apellido})'

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre} {self.apellido}"

    def __format__(self, format_spec):
        return f"{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}"

if __name__ == '__main__':
    persona1 = Persona('Andres', 'Cortina')
    print(f'{persona1!r}')
    print(persona1)
    print(f"{persona1}")
