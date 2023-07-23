from Producto import Producto


class Orden:
    contador_ordenes = 0
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.productos = list(productos)

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ""
        for producto in self.productos:
            productos_str += producto.__str__() + "|"
        return f"Orden: {self.id_orden}\nProductos: {productos_str}"

if __name__ == "__main__":
    producto1 = Producto("Ketchup", 1500)
    producto2 = Producto("PC", 2000000)
    producto3 = Producto("Cama", 150000)

    productos = [producto1, producto2]
    productos1 = [producto1, producto2,producto3]
    productos2 = [producto2, producto1,producto3]

    orden1 = Orden(productos)
    orden2 = Orden(productos1)
    orden3 = Orden(productos2)

    print(orden1)
    print(orden2)
    print(orden3)
