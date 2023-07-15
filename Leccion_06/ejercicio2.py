# Ejercicio 2: Funcion arg para multiplicar
def multiplicarArgs(*a):
    multiplicacion = 1
    for m in a:
        m = int(m)
        multiplicacion *= m
    return multiplicacion


resultado = multiplicarArgs(3, 5, 15)

print(resultado)
print(resultado)

