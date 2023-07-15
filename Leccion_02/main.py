# Ejercicio 9: Tienda de libros

# Entrada
print("Proporcione los siguientes datos del libro: ")
L_nombre = input("Proporciona el nombre: ")
L_ID = int(input("Proporciona el ID: "))
L_precio = float(input("Proporciona el precio: "))
esGratuito = input("Indica si el envio es gratuito (True/False): ")

# Comprovante
if esGratuito == "True":
    esGratuito = True
elif esGratuito == "False":
    esGratuito = False
else:
    esGratuito = "El valor no fue valido"

# Separador
print()

# Salida
print(f"Nombre: {L_nombre}")
print(f"Id: {L_ID}")
print(f"Precio: {L_precio}")
print(f"Envio Gratuito: {esGratuito}")
