# Definir funcion

def sumar(a,b):
    return a + b

# Asignacion a variable

mi_funcion = sumar

resultado = mi_funcion(45,5)
print(resultado)

# Funcion como argumento
def operacion(a, b, sumar):
    print(f"Resultado de la suma: {sumar(a, b)}")

operacion(4, 10, sumar)

# Retornar funcion entre funciones

def retornar_funcion():
    return sumar

sumas = retornar_funcion()
print(f"Suma {sumas(5, 6)}")