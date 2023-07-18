from Orden import *
from Producto import *

producto1 = Producto("Pantalon", 6000)
producto2 = Producto("camisas", 1200)
ordenes = [producto1, producto2]
orden1 = Orden(ordenes)
print(orden1)
print(f"Total de la orden 1:", {orden1.calcular_total()})
producto3 = Producto("Sueters", 5000)
ordenes2 = [producto3]
orden2 = Orden(ordenes2)
print(orden2)