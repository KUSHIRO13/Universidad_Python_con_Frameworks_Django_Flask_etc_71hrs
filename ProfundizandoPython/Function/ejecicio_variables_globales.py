# Definimos una variable global
contador = 0

def mostrar_contador():
    print(contador)


def modificar_contador(c):
    global contador
    contador = c


mostrar_contador()
modificar_contador(15)
mostrar_contador()
