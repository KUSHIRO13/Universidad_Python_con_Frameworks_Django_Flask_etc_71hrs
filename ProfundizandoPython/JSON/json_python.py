# Leer Archivo JSON
# JSON = Javascript Object Notation
import json
from urllib import request

URL = 'http://globalmentoring.com.mx/api/personas.json'
req = request.Request(URL,None,{
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
})

respuesta = request.urlopen(req)
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)

json_respuesta = json.loads(cuerpo_respuesta.decode('UTF-8'))
print(json_respuesta)

for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]} {persona["edad"]}')

# Accedemos a las variables independientes
print(f"Total personas: {json_respuesta['total']}")
print(f"Mensaje: {json_respuesta['mensaje']}")