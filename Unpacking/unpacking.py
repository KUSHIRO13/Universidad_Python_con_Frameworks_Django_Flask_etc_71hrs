# Unpacking
valores = 1, 2, 3
print(type(valores))
print(valores)

v1, v2, v3 = 1, 2, 3
print(v1, v2, v3)

# Se omiten valores con el guion bajo
v1, _, v3 = 1, 2, 3
print(v1, v3)
print(v1, _, v3)

v1, v2, *v3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(v1, v2, v3)

v1, v2, *v3, v4, v5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(v1, v2, v3, v4, v5)

v1, v2, *v3, v4, v5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(v1, v2, v3, v4, v5)
print(type(v3))
print(type(v2))


def regresa_datos():
    return 1, 2, 3


v1, v2, v3 = regresa_datos()
print(v1, v2, v3)

v1 = regresa_datos()
print(v1)

v1, *_ = regresa_datos()
print(v1, _)

help(str.partition)

hora,separador,minutos = "17:20".partition(":")
# print(type(variable))
print(hora,separador,minutos)