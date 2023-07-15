# Ejercicio 7: rango de edad entre los 20 y 30

edad = int(input("Introduce tu edad: "))

resultado = 20 <= edad < 30
print(resultado)
treinta = 30 <= edad < 40
print(treinta)

if resultado or treinta:
    print("Tienes una edad entre los \'20 y 30 años\'")
    if resultado:
        print("Tienes una edad entre los 20's")
    elif treinta:
        print("Tienes una edad entre los 30's")
else:
    print("No estas dentro del rango de los '20 y 30 años'")
    