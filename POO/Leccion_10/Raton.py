from DispositivoEntrada import DispositivoEntrada
class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self, entrada, marca):
        super().__init__(entrada, marca)
        Raton.contador_ratones += 1
        self.__idRaton = Raton.contador_ratones

    def __str__(self):
        raton = " Raton ".center(29,"=")
        return f"{raton}\nId: {self.__idRaton} \n{super().__str__()}"


if __name__ == "__main__":
    raton1 = Raton("USB", "Havit")
    print(raton1)
    raton2 = Raton("Cable", "Hp")
    print(raton2)