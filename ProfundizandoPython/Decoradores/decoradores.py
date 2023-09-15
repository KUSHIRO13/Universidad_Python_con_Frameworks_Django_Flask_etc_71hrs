# Un decarador es una funcion que recibe un funcion y que regresa otra

# 1. Funcion decorador  (a)
# 2. Funcion a decorar  (b)
# 3. Funcion decorada   (c)

# def funcion_decorador_a(funcion_a_decorar_b):
#     def funcion_decorada_c():
#         funcion_a_decorar_b()
#
#     return funcion_decorada_c
#
# @funcion_decorador_a
# def mostrar_mensaje():
#     print('Hola desde la funcion mensaje')
#
# mostrar_mensaje()

# con argumentos

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        resiltado = funcion_a_decorar_b(*args, **kwargs)
        return resiltado

    return funcion_decorada_c

@funcion_decorador_a
def sumar(a, b):
    return a + b

resultado = sumar(4 , 5)
print(resultado)

# Prueba
def r_numero(a):
    lista = []
    def funcion(b):
        largo = a(b)
        nonlocal lista # Variable local
        if largo > 2:
            lista = [1, 1]
            for n in range(2, largo):
                lista.append(lista[-1] + lista[-2])
        else:
            for n in range(largo):
                lista.append(1)
        return lista
    return funcion


@r_numero
def repetir(a):
    return a


resultado = repetir(15)
print(resultado)
