# Desempaquetar

numeros = [1, 2, 3]
print(numeros)
print(*numeros)
print(*numeros, sep="-")

def sumar(a,b,c):
    print(f"Resultado de la suma: {a + b + c}")

sumar(*numeros)

# Extraer algunos elementos
mi_lista = list(range(1,7))
a, *b, c, d = mi_lista
print(a, b, c, d)

# Unir Listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [lista1, lista2]
print(f"Lista de lista: {lista3}")

lista3 = [*lista1, *lista2]
print(f"Unir lista: {lista3}")

# Unir diccionarios
dic1 = {
    "A":1,
    "B":2,
    "C":3,
}
dic2 = {
    "D":4,
    "E":5,
    "F":6,
}
dic3 = {
    **dic1,
    **dic2
}
print(f"Unir dicionarios: {dic3}")

# Convertir lista a partir de un String
lista = [*"Hola Mundo"]
print(lista)
print(*lista, sep="")
