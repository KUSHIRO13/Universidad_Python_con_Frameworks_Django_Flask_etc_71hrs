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

