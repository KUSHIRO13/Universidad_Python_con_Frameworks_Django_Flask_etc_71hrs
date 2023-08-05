from manejo_archivo import ManejoArchivo

with open("prueba.txt", "r", encoding="UTF-8") as archivo:
    print(archivo.read())

with ManejoArchivo("prueba.txt") as archivo:
    print(archivo.read())