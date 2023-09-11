# False

# Number
valor = 0
resultado = bool(valor)
print(f"Valor: {valor} | Resultado: {resultado}")

# String
valor = ""
resultado = bool(valor)
print(f"Valor: {valor} | Resultado: {resultado}")

# List
valor = []
resultado = bool(valor)
print(f"Valor: {valor} | Resultado: {resultado}")

# Tuple
valor = ()
resultado = bool(valor)
print(f"Valor: {valor} | Resultado: {resultado}")

# Diccionary
valor = {}
resultado = bool(valor)
print(f"Valor: {valor} | Resultado: {resultado}")

# True

# Number
valor = 15
resultado = bool(valor)
print(f"Valor: {valor} | Resultado: {resultado}")

# String
valor = "Hola"
resultado = bool(valor)
print(f"Valor: {valor} | Resultado: {resultado}")

# List
valor = [15,16]
resultado = bool(valor)
print(f"Valor: {valor} | Resultado: {resultado}")

# Tuple
valor = (2,"Como estas")
resultado = bool(valor)
print(f"Valor: {valor} | Resultado: {resultado}")

# Diccionary
valor = {
    "edad":15
}
resultado = bool(valor)
print(f"Valor: {valor} | Resultado: {resultado}")

if bool(16):
    print("Regreso Verdadero")
else:
    print("Regreso falso")
