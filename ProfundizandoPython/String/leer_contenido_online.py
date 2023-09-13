# Leer contenido online
import urllib.request
from urllib.request import urlopen

# Variables
URL = "http://globalmentoring.com.mx/recursos/GlobalMentoring.txt"
palabras = []

# Obtener el encabezado
req = urllib.request.Request(URL,None,{
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'
    })

# with urlopen(req) as mensaje:
#     contenido = mensaje.read().decode("UTF-8")
#     print(contenido)
#
# with open("Pagina.txt","w", encoding="UTF-8") as archivo:
#     archivo = archivo.write(contenido)

# with urlopen(req) as mensaje:
#     for p in mensaje:
#         palabras_por_linea = p.decode("UTF-8").split()
#         # print(palabras_por_linea)
#         for palabra in palabras_por_linea:
#             palabras.append(palabra)
# print(palabras)

with urlopen(req) as mensaje:
    contenido = mensaje.read().decode("UTF-8")
    contar = contenido.count("Universidad")
    print(contenido.upper())
    print()
    print(contenido.lower())
    print()
    print(contar)

print("python" in contenido.lower())

# startswith - incia con
print("Inicia con:",contenido.lower().startswith("en globalmentoring.com.mx"))
# endswith - Termina con
print("Termina con:", contenido.lower().endswith("de globalmentoring.com.mx"))
