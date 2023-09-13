# Reemplazar contenido en un str
from urllib import request

# Obtener enlace
URL = "http://globalmentoring.com.mx/recursos/GlobalMentoring.txt"
req = request.Request(URL,None,{
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"
})

# Guardar Contenido
contenido = request.urlopen(req).read().decode()

# Remplazar
print(contenido.replace(" ","-"))

# Eliminar caracteres al inicio y final de una cadena
titulo = "*** Hola Mundo **"
print("Cadena original: ",titulo)
print("Cadena Modificada: ",titulo.strip("*"))

