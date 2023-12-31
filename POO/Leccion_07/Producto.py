class Producto:
    contador_producto = 0
    def __init__(self, nombre, precio):
        self.__id_producto = Producto._contador_productos()
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        return f"{Producto.separador(self)}\n" \
               f"ID: {self.__id_producto}\nNombre: {self._nombre}\nPrecio: {self._precio}" \
               f"\n{Producto.separador(self)}"

    def separador(self):
        return "=".center(20,"=")

    @classmethod
    def _contador_productos(cls):
        cls.contador_producto += 1
        return cls.contador_producto

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    # @property
    # def _id_producto(self):
    #     return self._id_producto

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    # @_id_producto.setter
    # def _id_producto(self, id_producto):
    #     self._id_producto = id_producto


if __name__ == "__main__":
    producto1 = Producto("Manzana", 1500)
    print(producto1)
    producto2 = Producto("Coca Cola", 3500)
    print(producto2)

