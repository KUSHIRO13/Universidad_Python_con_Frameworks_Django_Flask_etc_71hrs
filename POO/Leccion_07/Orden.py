from Producto import *

class Orden():
    contador_ordenes = 0
    def __init__(self, producto ):

        self.__id_ordenes = Orden._contador_ordenes()
        self._productos = list(producto)

    def __str__(self):
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__() + "\n"
        return f"Orden:{self.__id_ordenes}\nProductos: \n{productos_str}"

    def agregar_producto(self, extras):
        self._productos.append(extras)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio()
        return total

    @classmethod
    def _contador_ordenes(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    @property
    def producto(self):
        return self._productos

    @producto.setter
    def producto(self, producto):
        self._productos = producto

# if __name__ == "__main__":
#     producto1 = Producto("Pantalon", 6000)
#     producto2 = Producto("camisas", 1200)
#     ordenes = [producto1,producto2]
#     orden1 = Orden(ordenes)
#     print(orden1)
#     producto3 = Producto("Sueters", 5000)
#     # ordenes = [producto3]
#     orden2 = Orden(ordenes)
#     print(orden2)