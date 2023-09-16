import math

multiplicacion = (valor * valor for valor in range(4))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

suma = sum(valor * valor for valor in range(4))
print(suma)

lista = ['Juan', 'Perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

lista = ['Karla', 'Gomez']
generador = (str(lista.index(valor) + 1) + ' ' + valor for valor in lista)
print(next(generador))
print(next(generador))

contador = 0
def incrementar():
    global contador
    contador +=1
    return contador

generador = (f"{incrementar()}. {nombre}" for nombre in lista)
lista = list(generador)
print(lista)
