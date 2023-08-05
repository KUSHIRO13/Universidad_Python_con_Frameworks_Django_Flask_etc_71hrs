# Importaciones
import os


# Creation de la clase CatalogoPelículas
class CatalogoPeliculas:
    ruta_archivo = "películas.txt"  # Variable que contiene el Path del archivo
    contador_peliculas = 0  # Variable opcional para dar más personalizacion

    def __init__(self, pelicula):
        CatalogoPeliculas.contador_pelicula()  # Contador de las películas
        CatalogoPeliculas.agregar_pelicula(pelicula)  # Agregar películas

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, "a", encoding="UTF-8") as ap:  # Se abre el archivo y si no existe se crea
            ap.write(f"{CatalogoPeliculas.contador_peliculas}. {pelicula}\n")

    # Clase estática que hace un recuento
    @classmethod
    def contador_pelicula(cls):
        cls.contador_peliculas += 1
        return cls.contador_peliculas

    # Clase que crea una lista del archivo
    @classmethod
    def listar_peliculas(cls):
        try:  # Se utiliza el try cath por si es que el archivo no existe y evitar un error
            with open(cls.ruta_archivo, "r", encoding="UTF-8") as la:
                for lista in la:
                    print(lista, end="")  # Se utiliza el atributo end= para eliminar el salto de linea adicional
        except Exception as e:
            print(f"Se produjo un error de '{e}' porque el archivo no existe")

    # Creacion del metodo eliminar
    @classmethod
    def eliminar(cls):
        for arch in os.listdir():  # Se hace una lista de lo que contiene la carpeta
            if arch == cls.ruta_archivo:  # Si el archivo ha sido creado se eliminara
                os.remove(cls.ruta_archivo)
                print(f"Archivo eliminado: películas.txt")
                # Lo siguiente se debe repetir hasta que encuentre al menos una vez el archivo
            else:
                continue
        else:  # Y si nunca lo encontro se debe ejecutar esta línea
            print("El archivo no existe")

    # Retorno falso cuando se requiere terminar de ejecutar
    @classmethod
    def salir(cls):
        return False
