# Funciones
def calculadora(*num, operacion = 'sumar'):
    """
    Funcion anidada de una calculadora, por defecto este en sumar pero la puedes cambiar a
    restar
    multiplicar
    dividir
    :param num: Tupla de valores
    :param operacion: Operacion a realizar
    :return: Retorna la funcion sumar por defecto
    """
    # Funcion anidada
    def sumar(num):
        suma = 0
        for s in num:
            suma += s
        return suma

    def restar(num):
        resta = num[0]
        for r in num[1:]:
            resta -= r
        return resta

    def multiplicar(num):
        multi = 1
        for m in num:
            multi *= m
        return multi

    def dividir(num):
        divi = num[0]
        for d in num[1:]:
            divi /= d
        return divi

    if operacion == 'sumar':
        print(f'Las sumas son iguales a: {sumar(num)}')
    elif operacion == 'restar':
        print(f'La resta es igual a: {restar(num)}')
    elif operacion == 'multiplicar':
        print(f'La multiplicacion es igual a: {multiplicar(num)}')
    elif operacion == 'dividir':
        print(f'La division es igual a: {dividir(num)}')
    else:
        print('Valor invalido')


resultados = calculadora(56, 23, operacion='resta')
