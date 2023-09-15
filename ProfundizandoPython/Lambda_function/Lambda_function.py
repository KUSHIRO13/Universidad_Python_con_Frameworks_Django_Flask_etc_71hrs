def sumar(a, b):
    return a +b

mi_funcion = lambda a, b: a + b

resultado = mi_funcion(4, 5)
print(resultado)

# FUncion que no recibe argumentos
mi_funcion = lambda : 'Funcion sin argumentos'
print(mi_funcion())

# Funcion con parametros por default
mi_funcion = lambda a = 2, b = 3: a + b
print(f"Valor por default {mi_funcion(8)}")

# Funcion lambda con variables variables

mi_funcion = lambda *a, **b: len(a) + len(b)

print(f"Arggumentos variables: {mi_funcion(1, 3, 4, 3, a='Hola',b = 'como' )}")