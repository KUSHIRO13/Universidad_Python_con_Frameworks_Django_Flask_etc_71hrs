from Producto import Producto
from Orden import Orden


# Orden 1
producto1 = Producto("Television", 150000)
producto2 = Producto("Multitoma", 700000)
ordenes = [producto1,producto2]
orden = Orden(ordenes)

# Orden 2
orden2 = Orden(ordenes)

# Orden 3
producto3 = Producto("Microfono", 26000)
producto4 = Producto("Destornillador", 10000)
ordenes = [producto3, producto4]
orden3 = Orden(ordenes)

# Imprimir
print(orden)
print(orden2)
print(orden3)

# Agregar
print("Orden agregada")
orden.agregar_producto(producto4)
print(orden)
