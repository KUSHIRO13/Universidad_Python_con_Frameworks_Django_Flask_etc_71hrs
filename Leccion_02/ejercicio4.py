# Ejercicio 4: Valor dentro de un rango

rango = int(input("Ingrese un numero: "))

if rango == 0:
    print("El numero es igual a cero")
elif 0 < rango <= 5:
    print(f"El numero {rango} esta entre 0 y 5")
else:
    print(f"El numero {rango} esta fuera del rango")
