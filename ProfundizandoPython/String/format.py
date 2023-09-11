# Profundizando en string

# Dar formato
nombre = "Carlos"
edad = 19
sueldo = 3000
mensaje_con_formato = "Nombre: {}\nEdad: {}\nSueldo: {:.3f}".format(nombre,edad,sueldo)
print(mensaje_con_formato)

mensaje_con_formato = "Sueldo: {2:.2f}\nNombre: {0}\nEdad: {1}".format(nombre,edad,sueldo)
print(mensaje_con_formato)

mensaje_con_formato = "Nombre: {n}\nEdad: {e}\nSueldo: {s:.1f}".format(n = nombre,e = edad,s = sueldo)
print(mensaje_con_formato)

diccionario = {
    "nombre": "Ivan",
    "edad": 25,
    "sueldo": 8000.00
}
mensaje_con_formato = "Nombre: {persona[nombre]}\nEdad: {persona[edad]}, Sueldo: {persona[sueldo]:.2f}".format(persona=diccionario)
print(mensaje_con_formato)
