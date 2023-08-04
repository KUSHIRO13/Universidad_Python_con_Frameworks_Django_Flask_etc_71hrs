# Creacion de un archivo si no existe y abrirlo si existe
try:
    archivo = open("prueba.txt", "w", encoding="UTF-8")
    archivo.write("Hola como estas? yo me llamo Andrés")
    archivo.write("\nY adios")
except Exception as e:
    print(f"Ocurrió un error tipo {e}")
finally:
    if "archivo" in locals():
        archivo.close()
