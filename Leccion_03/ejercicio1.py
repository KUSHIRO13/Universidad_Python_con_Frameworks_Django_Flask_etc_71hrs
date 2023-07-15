# Ejercicio 1: Conversion de entero a texto

c_num = int(input("Propoerciona un valor del 1 al 3: "))
c_text = None

if c_num == 1:
    c_text = "Numero UNO"
elif c_num == 2:
    c_text = "Numero DOS"
elif c_num == 3:
    c_text = "Numero TRES"
else:
    c_text = "Valor invalido"

print(f"El numero proporcionado: {c_num} es {c_text}")