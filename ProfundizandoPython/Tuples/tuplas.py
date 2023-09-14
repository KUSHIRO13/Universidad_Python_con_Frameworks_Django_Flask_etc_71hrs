# Profundizando en tuplas

# Declara variables
a,b = "Hola", "adios"
print(a,b)

# Swap
a,b = b,a
print(a,b)


# Regresar multiples valores en una funcion

def min_max(*elementos):
    return min(elementos), max(elementos)

min,max = min_max(1,25,7,6,2,6,47,5)
print(f"Valor minimo: {min}")
print(f"Valor maximo: {max}")

# Regresar suma de la tuplas
resultado = sum(tuple(range(1, 5 + 1)))
print(resultado)

def suma(*suma):
    return sum(suma)
print(f"Suma: {suma(1,5,2,6,4,6,8,9,2)}")
