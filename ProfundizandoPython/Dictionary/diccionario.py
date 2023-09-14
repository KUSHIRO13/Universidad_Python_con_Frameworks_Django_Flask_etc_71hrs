from pprint import pprint as pp
# Profundizando en diccionario
diccionario = {
    'nombre': 'Carlos',
    'apellido': 'Gutierres',
    'edad': 19
}
print(diccionario)
# diccionario = {1: "Cinco"}
# print(diccionario)

diccionario['departamento'] = 'Sistemas'
print(diccionario)

print(diccionario["nombre"])

# Metodo get
def crear_dic():
    enviar = diccionario['Nombre'] = "Kushiro"
    return enviar
print(diccionario.get('Nombre', crear_dic()))

print(diccionario.setdefault('Nombres', 'Nande'))
print(diccionario)

help(pp)
pp(diccionario, sort_dicts=False)