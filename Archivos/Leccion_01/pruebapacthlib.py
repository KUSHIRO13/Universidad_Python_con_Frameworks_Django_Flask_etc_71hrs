from pathlib import Path, PurePath

#Saber ruta
ruta = Path.cwd()
print(ruta)
print(ruta)
print(type(ruta)) # Da una clase

# Listar carpetas
iterardirect = Path().iterdir()
iterardirect1 = Path("venv").iterdir()
print(list(iterardirect))
print(list(iterardirect1))

# Juntar rutas
rutapura = PurePath.joinpath(ruta, "venv/Lib")
print(rutapura)

# Crear carpetas
crercarpet = Path("HolaPath").mkdir(exist_ok=True)

# Crear carpeta sobre carpeta
pathcrear = PurePath.joinpath(Path.cwd(),"Konn", "ichiwa").mkdir(parents=True)
