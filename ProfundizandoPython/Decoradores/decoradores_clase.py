import inspect


def decorador_repr(cls):
    print('Se ejecuta el decorador')
    print(f'Recibimos el objeto {cls.__name__}')

    # Revisamos los atributos de la clase
    atributos = vars(cls)
    # for nombre, apellido in atributos.items():
    #     print(nombre, apellido)

    # Verificar la exiatencia de un parametro
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreecrito el metodo __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma del metodo init {firma_init}')

    # Recuperamos los parametros
    parametros_init = list(firma_init.parameters)[1:]
    print(parametros_init)

    # Revisamos si por cada parametro tienen un propoerty
    for parametros in parametros_init:
        propert = isinstance(atributos.get(parametros), property)
        if not propert:
            raise TypeError(f"No tiene property {parametros}")

    def metodo_repr(self):
        nombre_clase = self.__class__.__name__
        print(f"Nombre clase: {nombre_clase}\n"
              f"Atributo 1: {parametros_init[0]}\n"
              f"Atributo 2: {parametros_init[1]}\n")
        generador_argumentos = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        lista = list(generador_argumentos)
        print(f"Lista del generador {lista}")
        argumentos = ','.join(lista)
        print(argumentos)
        return f'Resultado de ejecutar el metodo repr'

    setattr(cls, '__repr__', metodo_repr)

    return cls
@decorador_repr
class Persona:
    def __init__(self, nombre, apellido):
        print('Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido




    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido


if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez')
    print(persona1)