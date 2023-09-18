class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def agregar_elemento(self, elemento):
        self._elementos.append(elemento)

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._elementos!r})'


class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # Ordenamos los elementos inicializados
        if elementos is None:
            elementos = []
        self.ordenar()

    def agregar_elemento(self, elemento):
        super().agregar_elemento(elemento)
        self.ordenar()

    @property
    def elemento(self):
        return self._elementos

    @elemento.setter
    def elemento(self, elementos):
        self._elementos = elementos


class ListaEntero(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)

        super().__init__(elementos)

    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'No es una valor entero {elemento}')
        # if elemento >= 0:
        #     return elemento
        # else:
        #     raise ValueError(f"Solo se aceptan numeros enteros")

    def agregar_elemento(self, elemento):
        self._validar(elemento)
        super().agregar_elemento(elemento)

# Lista de enterps ordenados
class ListaEnterosOrdenados(ListaEntero, ListaOrdenada):
    pass


if __name__ == '__main__':
    lista_simple = ListaSimple([5, 6, 8, 9, 2, 3])
    print(lista_simple)

    lista_ordenada = ListaOrdenada(lista_simple)
    print(lista_ordenada)
    lista_ordenada.agregar_elemento(-5)
    print(lista_ordenada)
    print(len(lista_ordenada))

    lista_entero = ListaEntero(lista_simple)
    print(lista_entero)
    lista_entero.agregar_elemento(5)
    print(lista_entero)

    lista_entero_ordenado = ListaEnterosOrdenados(lista_ordenada)
    print(lista_entero_ordenado)
    # Isinstance
    print(f'Es un entero {isinstance("10", int)}')
    print(f'Es una cadena {isinstance(10, str)}')
    print(f'Es una lista ordenada {isinstance(lista_entero_ordenado, ListaEnterosOrdenados)}')