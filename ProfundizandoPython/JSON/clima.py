import json
from urllib import request

URL = 'http://globalmentoring.com.mx/api/clima.json'

req = request.Request(URL, None, {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
})
respuesta = request.urlopen(req)
lectura = respuesta.read()

json_datos = json.loads(lectura.decode('UTF-8'))
print(json_datos)

# Obligatorias
for descripcion in json_datos['clima']:
    print(descripcion)
    print(f"El dia de hoy se presentan: {descripcion['descripcion']}")

for valor,llave in json_datos['principal'].items():
    if valor == 'temp_min':
        print(f"La temperatura minima es: {llave}")
    if valor == 'temp_max':
        print(f"La temperatura maxima es: {llave}")

# Solucion
descripcion = json_datos.get('clima')[0]
print(f"La descripcion del clima es {descripcion['descripcion']}")

temp_min = json_datos.get('principal')['temp_min']
print(f'La temperatura minima es {temp_min}')

temp_max = json_datos['principal'].get('temp_max')
print(f'La temperatura maxima es {temp_max}')
