import math
from decimal import Decimal

# Manejo de valores infinitos

# Usando float()
# infinito_positivo = float("inf")
# print(f"Infinito Positivo: {infinito_positivo}")
# print(f"Es Infinito Positivo?: {math.isinf(infinito_positivo)}")

# infinito_negativo = float("-inf")
# print(f"Infinito Negativo: {infinito_negativo}")
# print(f"Es Infinito Negativo?: {math.isinf(infinito_negativo)}")

# Usando math
# infinito_positivo = math.inf
# print(f"Infinito Positivo: {infinito_positivo}")
# print(f"Es Infinito Positivo?: {math.isinf(infinito_positivo)}")
#
# infinito_negativo = -math.inf
# print(f"Infinito Negativo: {infinito_negativo}")
# print(f"Es Infinito Negativo?: {math.isinf(infinito_negativo)}")

# Usando Decimal
infinito_positivo = Decimal("Infinity")
print(f"Infinito Positivo: {infinito_positivo}")
print(f"Es Infinito Positivo?: {math.isinf(infinito_positivo)}")

infinito_negativo = Decimal("-Infinity")
print(f"Infinito Negativo: {infinito_negativo}")
print(f"Es Infinito Negativo?: {math.isinf(infinito_negativo)}")
