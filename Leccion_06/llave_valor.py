def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")


dicionario = {
    "IDE": "Integrated Development Enviroment",
    "PK": "Primary Keys"
}

listarTerminos(IDE="Integrated Development Enviroment", PK="Primary Keys")
