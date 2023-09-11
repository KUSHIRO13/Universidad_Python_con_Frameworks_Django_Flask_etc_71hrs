from mi_clase import MiClase
# Profundizando en el tipo str

# Concatenacion
mensaje = "Hola" + " mundo"
print(mensaje)

mensaje = "Hola" " mundo"
print(mensaje)

mensaje += ", como estas"
print(mensaje)

# help(str)
print(MiClase.__doc__)
print(MiClase.__init__.__doc__)
print(MiClase.mi_metodo.__doc__)

# Inmutable
help(str.capitalize)

mensaje1 = "hola mundo"
mensaje2 = mensaje1.capitalize()
print(f"mensaje1: {mensaje1}, id: {hex(id(mensaje1))}")
print(f"mensaje2: {mensaje2}, id: {hex(id(mensaje2))}")

mensaje1 += ", Adios"
print(f"mensaje1: {mensaje1}, id: {hex(id(mensaje1))}")


help(str.join)
mensaje1 = "Hola"
mensaje2 = "como"
mensaje3 = "estas"
mensaje4 = ("Hola", "como", "te", "va", "en", "el", "SENA")
print(" ".join([mensaje1,mensaje2,mensaje3]))
print("-".join(mensaje4))

lista_cursos = ["Python", "CSS", "HTML", "Javascript"]
mensaje5 = "Los lenguajes que conosco son: "
mensaje5 += ", ".join(lista_cursos)
print(mensaje5)

cadena = "HolaMundo"
mensaje = ".".join(cadena)
print(mensaje)


diccionario = {
    "nombre" : "Carlos",
    "apellido" : "Cortina",
    "edad:" : "19"
}

llaves = "-".join(diccionario.keys())
valores = "*".join(diccionario.values())
print(llaves)
print(valores)

# split

help(str.split)

cursos = "Java Python Javascript HTML CSS Excel"
lista_cursos = []
lista_cursos = cursos.split()
print(lista_cursos)

cursos_comas = "Java, Python, Javascript, HTML, CSS, Excel"
lista_cursos = cursos_comas.split(", ")
print(lista_cursos)

cursos_comas = "Java, Python, Javascript, HTML, CSS, Excel"
lista_cursos = cursos_comas.split(", ", maxsplit=2)
print(lista_cursos)


