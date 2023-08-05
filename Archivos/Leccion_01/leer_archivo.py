import os
try:
    archivo = open(f"{os.getcwd()}/Prueba.txt", "r", encoding="UTF-8")
    # Lee todos el archivo
    # print(archivo.read())

    #Leer alguno caracteres
    # print(archivo.read(5))
    # print(archivo.read(3))
    # print(archivo.read(3))

    # Leer lineas completas
    print(archivo.readline())
except Exception as e:
    print(f"Error tipo {e}")
finally:
    if "Prueba.txt" in locals():
        archivo.close()