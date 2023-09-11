import math
from decimal import Decimal

# NaN: Not a Number (No es un numero)
# No es sencible a mayusculas
# Tipo de dato numerico indefinido

# Usando float
a = float("NaN")
print(f"NaN: {a}")
print(f"es NaN?: {math.isnan(a)}")

# Usando Decimal
a = Decimal("NaN")
print(f"NaN: {a}")
print(f"es NaN?: {math.isnan(a)}")

