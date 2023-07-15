# Ejercicio 4: Sistema de Calificaciones

calificacion = float(input("Ingrese el valor de su calificacion: "))
nota = None

if 10 >= calificacion >= 9:
    nota = "A"
elif 9 > calificacion >= 8:
    nota = "B"
elif 8 > calificacion >= 7:
    nota = "C"
elif 7 > calificacion >= 6:
    nota = "D"
elif 6 > calificacion >= 0:
    nota = "F"
else:
    nota = "Valor desconocido"

print(f"Por haber sacado {calificacion} puntos tu nota sera {nota}")

