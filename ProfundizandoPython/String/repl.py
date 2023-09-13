class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"ID: {hex(id(self)).upper()}\nNombre: %s\nApellido: %s"%(self.nombre,self.apellido)


if __name__ == "__main__":
    persona1 = Persona("Juan", "Guzman")
    print(persona1)

def mostrar_mensaje(m):
    print(m)