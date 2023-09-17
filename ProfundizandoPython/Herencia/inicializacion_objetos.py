class Padre:
    def __init__(self):
        print('Inicializador Padre')
        
    def metodo(self):
        print('Metodo Padre')


class Hijo(Padre):
    # Se manda a llamar la clase __init__ del padre mientras que no se llame la del padre
    def __init__(self):
        super().__init__()
        print('Iniciador Hijo')
        
    def metodo(self):
        print('Metodo sobreescrito en Hijo')
if __name__ == '__main__':
    padre1 = Padre()
    padre1.metodo()
    
    hijo1 = Hijo()
    hijo1.metodo()
    # hijo1.metodo()
    