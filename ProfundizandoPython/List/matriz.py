# Matriz
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f"Matriz Original: {matriz}")
print(f"renglon 0 columna 0: {matriz[0][0]}")
print(f"renglon 2 columna 2: {matriz[2][2]}")
print(f"renglon 2 columna 3: {matriz[2][3]}")


lista_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]
lista_listas.sort(key=len)
print(f"Orden por tamaño: {lista_listas}")

# help(sorted)

nombre1 = ["Juan Carlos", "Karla", "Pedro", "Esperanza"]
nombre1 = sorted(nombre1)
print(nombre1)

nombre1 = ["Juan Carlos", "Karla", "Pedro", "Esperanza"]
nombre1 = sorted(nombre1, reverse=True)
print(nombre1)

# Ordenar por la cantidad de elementos
nombre1.sort(key=len)
print(nombre1)

# Reversed
nombre1 = reversed(nombre1)
print(list(nombre1))