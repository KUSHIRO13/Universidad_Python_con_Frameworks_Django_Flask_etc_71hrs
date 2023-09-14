# Alcanlce de variables (Scope)

var_global = 'Variable Global'


def imprimir():
    global var_global
    print(f"Variables global desde un funcion {var_global}")
    var_local = 'Variable Local'
    print(f"Variables global desde un funcion {var_local}")
    def funcion_anidad():
        print(f"Variables global desde una funcion anidada {var_local}")

    var_global = 'Hola'
    print(f"Nuevo valor de la variable global: {var_global}")
    funcion_anidad()
imprimir()
