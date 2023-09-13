# Profundizando en listas
# Creacion de listas
# Nombres
nombres1 = ["Carlo","Juan","Andres"]
nombres2 = "Laura Maria Gonzalo Hernesto".split()

# Numeros
numeros1 = [10, 40, 15, 4, 20, 90, 4]

# Suma de listas
print(f"Sumar listas:\t\t{nombres1 + nombres2}")

# Extender una lista
nombres1.extend(nombres2)
print(f"Extender listas:\t{nombres1}")

# Regresar indice
# help(list.index)
print(f"Indice de 4: {numeros1.index(4)}")

# Invertir orden de lista
print(f"Lista originales:\t{numeros1}")
numeros1.reverse()
print(f"Lista invertida:\t{numeros1}")

# Ordenar elemento
numeros1.sort()
print(f"Lista ordenada asc:\t{numeros1}")
numeros1.sort(reverse=True)
print(f"Lista ordenada desc:{numeros1}")

# Valor minimo
print(f"Valor minimo:\t\t{min(numeros1)}")
print(f"Valor Maximo:\t\t{max(numeros1)}")

# lista Copiada
nombres3 = nombres2.copy()
print(f"Lista copiada:\t\t{nombres3} id1: {hex(id(nombres2))} id1: {hex(id(nombres3))}")
print(f"Mismo referencia?:\t{nombres3 is nombres2}")
print(f"Mismo contenido?:\t{nombres3 == nombres2}")

# Slicing
numeros2 = numeros1[:]
print(numeros2)
print(f"Mismo referencia?:\t{numeros1 is numeros2}")
print(f"Mismo contenido?:\t{numeros1 == numeros2}")

# Multiplicacion de listas
lista_multiplicada = 5*[[2,5]]
print(lista_multiplicada)
lista_multiplicada[2].append(10)
print(f"Tienen la misma referencia?: {lista_multiplicada[0] is lista_multiplicada[1]}")
print(f"Tienen el mismo contenido?: {lista_multiplicada[0] == lista_multiplicada[1]}")
print(lista_multiplicada)





