from Computadora import Computadora, Monitor, Teclado, Raton
from Orden import  Orden

# Creacion de los monitores
monitor1 = Monitor("Acer", "12 pulgadas")
monitor2 = Monitor("Toshiba", "15 pulgadas")
monitor3 = Monitor("DELL", "25 pulgadas")

# Creacion del teclado
teclado1 = Teclado("Integrado", "Acer")
teclado2 = Teclado("Integrado", "Toshiba")
teclado3 = Teclado("USB", "DELL")

# Creacion del raton
raton1 = Raton("USB", "Havit")
raton2 = Raton("USB", "Wabit")
raton3 = Raton("PS/2", "DELL")

# Creacion de las computadoras
computadora1 = Computadora("Acer",monitor1,teclado1,raton1)
computadora2 = Computadora("Toshiba", monitor2, teclado2, raton2)
computadora3 = Computadora("DELL", monitor3, teclado3, raton3)

# Creacion de los pedidos
pedido1 = [computadora1]
pedido2 = [computadora2]
pedido3 = [computadora1, computadora2]
pedido4 = [computadora3]

# Creacion de la orden
orden1 = Orden(pedido1)
orden2 = Orden(pedido2)
orden3 = Orden(pedido3)
orden4 = Orden(pedido4)

# Impresiones
print(orden1)
print(orden2)
print(orden3)
print(orden4)

# Agregaciones
orden4.agregar_computadora(computadora1)

# Segunda impresion
print("Segunda impresion")
print(orden4)

