from DispositivoEntrada import DispositivoEntrada
class Teclado(DispositivoEntrada):
    contador_teclado = 0
    def __init__(self, entrada, marca):
        super().__init__(entrada, marca)
        Teclado.contador_teclado += 1
        self.__idTeclado = Teclado.contador_teclado

    def __str__(self):
        teclado = " Teclado ".center(29,"=")
        return f"{teclado}\nId: {self.__idTeclado}\n{super().__str__()}"


if __name__ == "__main__":
    teclado1 = Teclado("Bluetooh","Gamer")
    print(teclado1)
    teclado2 = Teclado("USB", "Acer")
    print(teclado2)