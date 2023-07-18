from Cuadrado import *
from Rectangulo import *


print(" Cuadrados ".center(40,"="))
cuadrado = Cuadrado(5, "Rojo")
# print(cuadrado.alto)
# print(cuadrado.ancho)
# print(f"El color del cuadrado es: " + cuadrado.color)
# print(f"El area del cuadrado es: ",cuadrado.calcular_area())

# MRO Method Resolution Order
print(cuadrado)

cuadrado2 = Cuadrado(lado= 6, color= "Morado")
cuadrado3 = Cuadrado(15, "Naranja")
cuadrado4 = Cuadrado(2, "Rojo")

print(cuadrado2)
print(cuadrado3)
print(cuadrado4)

print(" Rectangulos ".center(50, "="))
rectangulo1 = Rectangulo(5,9, "Cielo")
rectangulo2 = Rectangulo(6, 9, "Negro")
rectangulo3 = Rectangulo(8, 2, "Azul Cielo")
rectangulo4 = Rectangulo(5, 4, "Purpura")

print(rectangulo1)
print(rectangulo2)
print(rectangulo3)
print(rectangulo4)