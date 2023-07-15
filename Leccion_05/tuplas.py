# Definir una tupla
frutas = ("Naranja", "Platano", "Guayaba")

# Funciones
# Largo
print(len(frutas))
# Acceder elemento
print(frutas[0])
# Navegacion inversa
print(frutas[-1])
# Navegacion por rango
print(frutas[:-1])
# Recorrer tuplas
for f in frutas:
    print(f, end=" ")
# Convercion
Frutalistas = list(frutas)
Frutalistas[0] = "Pera"
frutas = tuple(Frutalistas)
print()
print(frutas)

