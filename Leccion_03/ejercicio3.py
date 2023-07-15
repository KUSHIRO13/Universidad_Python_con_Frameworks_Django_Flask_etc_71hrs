# Ejercicio 3: Etapas de vida segun edad

edad = int(input("Proporciona tu edad: "))

if 0 <= edad < 10:
    print("La infancia es increible...")
elif 10 <= edad < 20:
    print("Muchos cambios y muchos estudios...")
elif 20 <= edad <= 30:
    print("Amor y comienza el trabajo...")
else:
    print("Etapa de vida no reconocida")