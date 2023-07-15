# Ejercicio 2: Calcular la estacion del año segundo el numero del mes

n_mes = int(input("Proporciona mes del año (1-12): "))
estacion = None

if n_mes == 1 or n_mes == 2 or n_mes == 12:
    estacion = "Invierno"
elif 3 <= n_mes <= 5:
    estacion = "Primavera"
elif 6 <= n_mes <= 8:
    estacion = "Verano"
elif 9 <= n_mes <= 11:
    estacion = "Otoño"

print(f"El valor {n_mes} corresponde a la estacion de {estacion}") if 1 <= n_mes <= 12 else print("Valor incorrecto")
