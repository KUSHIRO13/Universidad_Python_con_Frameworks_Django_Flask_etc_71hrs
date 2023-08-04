import os

# Saber ruta
ruta = os.getcwd()
print(ruta)
print(type(ruta)) # Os da un texto

# Listar carpetas
listadirectorio = os.listdir() #
listadirectorio1 = os.listdir("venv") #
print(listadirectorio)
print(listadirectorio1)

# Juntar rutas
juntarutas = os.path.join(ruta, "venv")
print(juntarutas)

# Crear carpetas
# crearCap = os.mkdir("Hola")

# Crear carpetas sobre carpetas
crearCapsobrecaro = os.makedirs(os.path.join("MakeDirs", "Hola"))
