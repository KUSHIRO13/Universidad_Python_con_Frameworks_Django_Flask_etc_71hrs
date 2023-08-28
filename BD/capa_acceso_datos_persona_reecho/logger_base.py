import logging

log = logging

log.basicConfig(level=log.DEBUG,
                format="[%(levelname)s] %(asctime)s (%(filename)s-%(lineno)s): %(message)s",
                datefmt="%I:%M:%S %p",
                handlers=[
                    log.FileHandler("Datos.log"),
                    log.StreamHandler()
                ])

if __name__ == "__main__":
    log.info("Esta es una prueba de INFO")