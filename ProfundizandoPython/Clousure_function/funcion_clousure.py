# Un closure en una funcion que define a otra

# Funcion principal

def operacion(a, b):
    # Definimos una funcion anidada
    def sumar():
        return a + b

    return sumar


mi_funcion = operacion(5, 6)
print(f"Resultado de la funcion {mi_funcion()}")

# Llamar la funcion
print(f'Resultado de la funcion: {operacion(2, 3)()}')

# Funcion lambda
def operacion(a, b): return lambda: a - b

mi_funcion = operacion(15, 6)
print(f"Resultado de la funcion lambda {mi_funcion()}")

# Llamar la funcion
print(f'Resultado de la funcion lambda: {operacion(16, 3)()}')
