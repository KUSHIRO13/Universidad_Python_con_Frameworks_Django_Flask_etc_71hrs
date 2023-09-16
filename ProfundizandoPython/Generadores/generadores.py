# Generadores

def generador():
    yield 1
    yield 2
    yield 3

gen = generador()

print(next(gen))
print(next(gen))
print(next(gen))
print(type(gen))

gen = generador()
for valor in generador():
    print(valor)