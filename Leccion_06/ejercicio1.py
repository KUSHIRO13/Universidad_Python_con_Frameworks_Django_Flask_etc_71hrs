# Ejercicio 1: Funcion arg para sumar
def sumarArgs(*a):
    suma = 0
    for s in a:
        s = float(s)
        suma += s
    return suma

resultado = sumarArgs(12,3,5,6,8,6,2.25)
print(resultado)
