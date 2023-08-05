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
# crearCapsobrecaro = os.makedirs(os.path.join("MakeDirs", "Hola"))

# Renombrar archivos
# renombrar = os.rename("Hola", "OsHola")
i = 0
for file in os.listdir():
    i += 1
    if file.endswith(".txt"):
        os.rename(file,f"{file} {i}")

# Comprobacion de existencia
existe = os.path.exists("Konn")
print(existe)

# Meta data

metadata = os.path.abspath("MakeDirs")
print(metadata)
metadata = os.path.getsize("cueva.txt 2")
print(metadata)
