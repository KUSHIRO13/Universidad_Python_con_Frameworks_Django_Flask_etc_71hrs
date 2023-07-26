# Creacion de la clase padre
class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    def __str__(self):
        return f"Caracteristicas\nTipo de entrada: {self._tipoEntrada}" \
                                 f"\nMarca: {self._marca}"

    # Metodos Get y Sets
    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @property
    def marca(self):
        return self._marca


    @tipoEntrada.setter
    def tipoEntrada(self, entrada):
        self._tipoEntrada = entrada

    @marca.setter
    def marca(self, marca):
        self._marca = marca