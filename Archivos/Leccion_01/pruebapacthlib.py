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
# pathcrear = PurePath.joinpath(Path.cwd(),"Konn", "ichiwa").mkdir(parents=True)

# Renombrar archivos
# carpetaobjetivo = Path("HolaPath")
# carpetaActual = Path("HolaPath2")
#
# Path.rename(carpetaobjetivo,carpetaActual)

# Comprobar si existe
arch = Path("OsHola")
print(arch.exists())

script = Path("pruebaos.py")
print(script.resolve())
print(script.stem)
print(script.suffix)
if script.suffix == ".py":
    print("es un archivo de python")
print(script.stat().st_size)

