# Set

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

# Largo
print(len(planetas))

# Esta dentro
print("Marte" in planetas)

# Agregar elemento
planetas.add("Tierra")
print(planetas)

# No soporta duplicados
planetas.add("Tierra")
print(planetas)

# Remover
planetas.remove("Tierra") # Tambien se puede eliminar un elemento con discard
print(planetas)

# Limpiar
planetas.clear()
print(planetas)

# eliminar set
del planetas
