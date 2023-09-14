# Profundizar en sets
conjunto = {1,2,3,4}
print(conjunto)

# Sets vacio
conjunto = set()
print(type(conjunto))

# Agregar
conjunto.add("Juan")
print(conjunto)

conjunto = set([1,5,9,6,1,5,36,5])
print(type(conjunto))
print(conjunto)
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)

# Copiar conjunto
copia = conjunto.copy()
print(copia)

print(conjunto == copia)
