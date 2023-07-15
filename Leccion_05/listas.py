nombres = ["Juan", "Karla", "Ricardo", "Maria",]

print(nombres[-1])
print(nombres[0:2 + 1])
print(nombres[:3])
print(nombres[2:])

nombres[3] = "Andres"
print(nombres)

for l in nombres:
    print(l)
else:
    print("Ya no hay mas nombres en la lista")

print(len(nombres))

# Agregar un elemento

nombres.append("Kushiro")
print(nombres)

# Insertar un elemento en algun indice

nombres.insert(2, "Mafalda")
print(nombres)

# Remover un elemento

nombres.remove("Mafalda")
print(nombres)

# Remover el ultimo
nombres.pop()
print(nombres)

# Eliminar por indixe

del nombres[0]
print(nombres)

# Limpiar
nombres.clear()
print(nombres)

#Borrar lista
del nombres
print(nombres)