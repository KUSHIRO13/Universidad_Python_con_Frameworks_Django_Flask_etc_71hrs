# Creacion de clase Pelicula
class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return self._nombre # Se retorno el nombre de la pelicula
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre