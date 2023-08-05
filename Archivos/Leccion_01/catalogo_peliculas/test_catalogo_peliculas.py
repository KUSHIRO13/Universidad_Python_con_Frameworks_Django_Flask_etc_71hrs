# Importaciones
from catalogo_peliculas.dominio.pelicula import Pelicula
from catalogo_peliculas.servicio.catalogopeliculas import CatalogoPeliculas

if __name__ == "__main__":
    # Declaraciones
    salir = True

    print(" Inicio del programa ".center(50, "="))
    while salir: # Se repite hasta que salir sea falso
        opciones = input("1) Agregar película\n2) Listar películas\n3) Eliminar archivo de películas\n4) Salir\n>>: ")
        if opciones == "1":
            a_pelicula = input("Como se llama la película: ")
            peliculas = Pelicula(a_pelicula)
            CatalogoPeliculas(peliculas)
        elif opciones == "2":
            CatalogoPeliculas.listar_peliculas()
        elif opciones == "3":
            CatalogoPeliculas.eliminar()
        elif opciones == "4":
            salir = CatalogoPeliculas.salir()
        else:
            print("Favor digitar un numero del (1-4)")
    else:
        print(" Fin del programa ".center(50, "="))
