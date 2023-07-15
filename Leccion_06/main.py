# Ejercicio 5: Conversor de temperaturas
# Funcion que convierte grados de Celcius a Farenheit
def celsiusFahrenheit(c):
    return c * 1.8 + 32


# Funcion que convierte grado de Farenheit a Celsius
def fahrenheitCelsius(f):
    return (f - 32) / 1.8


# Declaracion de variables
grados = ["Celsius", "Fahrenheit"]
unidad = None
cantidad = None

# Entrada de datos
opcion = input(f"""
Proporcione la unidad que deseas convertir
1 - {grados[0]}
2 - {grados[1]}
>>: """)

# Comprobaciones
if opcion == "1" or opcion == "2":
    cantidad = float(input("Ingrese el grado a convertir: "))
    if opcion == "1":
        unidad = celsiusFahrenheit(cantidad)
    elif opcion == "2":
        grados.reverse()
        unidad = fahrenheitCelsius(cantidad)
else:
    print("Valor incorrecto")

# Salida Final de datos
if opcion == "1" or opcion == "2":
    print(f"El convertir {cantidad} {grados[0]} a {grados[1]} es {unidad}°")