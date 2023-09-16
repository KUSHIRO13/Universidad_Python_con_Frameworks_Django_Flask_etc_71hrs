def gernerador_numeros():
    for n in range(1, 5):
        yield n
        print('Se reanuda la ejecuacion')

generador = gernerador_numeros()


for n in generador:
    print(n)


generador = gernerador_numeros()
print(next(generador))
print(next(generador))