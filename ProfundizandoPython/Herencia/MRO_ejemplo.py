class Clase1:
    def __init__(self):
        print(f'{self.__class__.__name__}.__init__ En Clase 1')

    def metodo(self):
        print('Metodo Clase 1')


class Clase2(Clase1):
    def __init__(self):
        print(f'{self.__class__.__name__}.__init__ (Sobreescrito en Clase 2)')
        super().__init__()
    def metodo(self):
        print('Metodo Clase 2')
        super().metodo()

class Clase3(Clase1):
    def __init__(self):
        print(f'{self.__class__.__name__}.__init__ (Sobreescrito en Clase 3)')
        super().__init__()
    def metodo(self):
        print('Metodo Clase 3')
        super().metodo()

class Clase4(Clase2, Clase3):
    def metodo(self):
        print('Metodo Clase 4')
        super().metodo()


if __name__ == '__main__':
    clase4 = Clase4()
    print(Clase4.__bases__)
    print(Clase4.mro())
    clase4.metodo()