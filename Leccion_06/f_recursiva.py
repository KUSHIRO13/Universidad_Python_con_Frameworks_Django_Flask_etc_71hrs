def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n - 1)

factor = 5
print(f"El factorial de {factor} es: {factorial(factor)}")