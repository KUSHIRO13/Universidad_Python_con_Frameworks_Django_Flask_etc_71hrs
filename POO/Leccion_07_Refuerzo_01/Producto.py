class Producto:
    contador_producto = 0

    def __init__(self, nombre, precio):
        Producto.contador_producto += 1
        #TODO: Encapsular las variables id_producto, nombre
        self.id_producto = Producto.contador_producto
        self.nombre = nombre
        self._precio = precio

    def __str__(self):
        return f"\nID producto: {self.id_producto}\nNombre: {self.nombre}\nPrecio: {self._precio}"

    # Decoradores
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self.precio = precio

if __name__ == "__main__":
    producto1 = Producto("Ketchup", 1500)
    print(producto1)
    producto2 = Producto("PC", 2000000)
    print(producto2)