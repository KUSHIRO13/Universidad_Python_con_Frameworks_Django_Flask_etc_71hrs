# Profundizando en string

# Dar formato
nombre = "Carlos"
edad = 19
mensaje_con_formato = "Mi nombre es %s y tengo %d años" % (nombre, edad)
print(mensaje_con_formato)

persona = ("Carla", "Gomez", 5000)
mensaje_con_formato = "Hola %s %s tu sueldo es $%.2f" % persona
print(mensaje_con_formato)
mensaje_con_formato = "Hola %s %s tu sueldo es $%.2f"
print(mensaje_con_formato % persona)
