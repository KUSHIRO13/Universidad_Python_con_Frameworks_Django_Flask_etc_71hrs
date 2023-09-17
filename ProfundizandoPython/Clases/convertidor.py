class ConvertidorTemperaturas:
    MAX_CELCIUS = 100.0
    MAX_FARENHEIT = 213.0

    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELCIUS:
            raise ValueError(f"Temperatura en Celsius demaciado alta {celsius}")
        return celsius * 9/5 + 32

    @classmethod
    def f_c(cls, farenheit):
        if farenheit > cls.MAX_FARENHEIT:
            raise ValueError(f"Temperatura en Farenheit demaciado alta {farenheit}")
        return (farenheit - 32) * 5/9

if __name__ == '__main__':
    celsius = ConvertidorTemperaturas.c_f(15)
    print(celsius)
    farenheit = ConvertidorTemperaturas.f_c(195)
    print(f'{farenheit:.2f}')
