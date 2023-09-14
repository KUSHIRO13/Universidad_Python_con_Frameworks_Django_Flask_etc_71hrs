# Personas con distintas caracteriticas
pelo_negro = {"Juan",'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}

# Todos los elementos con ojos color cafe y rubio (Union)
print(f"Union: {ojos_cafe.union(pelo_rubio)}")

# Se recupera solo los elementos que se encuentren en ambos conjuntos (Intersepcion)
print(f"Intersepcion: {ojos_cafe.intersection(pelo_rubio)}")

# Pelo negro sin ojos color cafe (Difference)
print(f"Diferentes: {pelo_rubio.difference(ojos_cafe)}")

# Pelo negro o ojos cafes
print(f"Diferencia simetrica: {pelo_negro.symmetric_difference(ojos_cafe)}")

# Preguntar si un set esta contenido en otro set (subset)
print(menores_30.issubset(pelo_negro))

# Preguntar si un set esta contenido en otro set (superset)
print(menores_30.issuperset(pelo_negro))

# Preguntar si los de pelo negro no tienen pelo rubio (dis joint)
print(pelo_negro.isdisjoint(pelo_rubio))
