resultado = None
a = "10"
b = 0
try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    resultado = a/b
except ValueError:
    print("Solo debes ingresar numeros")
except ZeroDivisionError:
    print(f"las opciones {a} y {b} no se pueden dividir")
except TypeError:
    print("Los valores no concuerdan")
except Exception as e:
    print(f"Ocurrio un error {e}")
else: # Se lanza cuando no ocurre ningan exepcion o error
    print(f"Resultado = {resultado}")
finally: # Siempre se ejecuta
    print("Bloque finally")
    print("continuamos...")
