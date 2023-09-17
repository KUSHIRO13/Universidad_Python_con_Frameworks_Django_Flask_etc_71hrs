numeros = range(10 + 1)
lista_pares = []

for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero * numero)

print(f'Lista de pares: {lista_pares}')

# Ahora con list comprehensions

lista_pares = []
lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]
print(lista_pares)

pares = []
pares = [numero for numero in range(50 + 1) if numero % 2 == 0 if numero % 6 == 0]
print(pares)

lista_pares = []
lista_impares = []
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)


print(lista_pares)
print(lista_impares)

lista_pares = []
lista_impares = []

[lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero) for numero in range(10)]
print(lista_pares)
print(lista_impares)


lista_lista = [[1, 2, 3],[4, 5, 6],[7, 8, 9, 10]]

lista_simple = [numero for sublista in lista_lista for numero in sublista]
print(lista_simple)

lista_pares = []

for lista in lista_lista:
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)

print(lista_pares)

lista_pares = []
lista_pares = [numero for lista in lista_lista for numero in lista if numero % 2 == 0]
print(lista_pares)