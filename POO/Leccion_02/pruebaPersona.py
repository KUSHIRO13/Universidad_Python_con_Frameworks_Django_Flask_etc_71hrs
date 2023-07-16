from Persona import Persona

if __name__ == "__main__":
    print(" Creacion de objectos ".center(50,"*"))
    persona1 = Persona("Karla", "Gomez", 26)
    print(persona1.mostrar_detalle())
    print(__name__)

    print(" Eliminar objetos ".center(50,"*"))
    del persona1


