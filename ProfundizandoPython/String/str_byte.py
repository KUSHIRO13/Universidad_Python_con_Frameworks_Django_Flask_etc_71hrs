# Profundizando en python

# Byte

string = "Programación con Python"
print(f"String original: {string}")
bytes = string.encode("UTF-8")
print(f"Bytes codificado: {bytes}")

string2 = bytes.decode("UTF-8")
print(f"Bytes codificado: {string2}")

