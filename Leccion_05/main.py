# Diccionarios

diccionario = {
    "IDE" : "Integrated Development Environment",
    "OOP" : "Object Oriented Programming",
    "DBMS" : "Database Management System"
}
print(diccionario)

# Largo
print(len(diccionario))

# Acceder
print(diccionario["IDE"])
# Otra forma de acceder
print(diccionario.get("OOP"))
# Modificar
diccionario["IDE"] = "integrated development environment"
print(diccionario)
# Recorrer
for dic,val in diccionario.items():
    print(dic,val)

for dic in diccionario.keys():
    print(dic)

for val in diccionario.values():
    print(val)

# Existencia
print("IDE" in diccionario)
print("IDe" in diccionario)

# Agregar un elemento
diccionario["PK"] = "Primary Keys"
print(diccionario)

# Remover
diccionario.pop("DBMS")
print(diccionario)

# Limpiar
diccionario.clear()
print(diccionario)

# Eliminar dicionario
del diccionario
