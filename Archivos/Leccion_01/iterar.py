try:
    archivo = open("prueba.txt", "r", encoding="UTF-8")
    ## Iteracion
    # for linea in archivo:
    #     print(linea)
    # print(archivo.readlines()[1])
    # Abrir un nuevo archivo
    archivo2 = open("copia.txt", "a", encoding="UTF-8")
    archivo2.write(archivo.read())

except Exception as e:
    print(f"Ocurrio un error tipo '{e}'")
finally:
    if "prueba.txt" in locals():
        archivo.close()
        archivo2.close()