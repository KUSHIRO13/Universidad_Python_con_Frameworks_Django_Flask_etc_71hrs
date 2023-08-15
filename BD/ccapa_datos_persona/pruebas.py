import logging

log = logging
log.basicConfig(
    level=log.DEBUG,
    format="%(asctime)s: %(levelname)s [%(filename)s-%(lineno)s]: %(message)s",
    datefmt="%I:%M:%S %p",
    handlers=[
        log.FileHandler("capa_prueba.log"),
        log.StreamHandler()
    ])

if __name__ == "__main__":
    log.debug("Esto es un debug")
    log.info("Esto es un info")
    log.error("Esto es un error")
    log.critical("Esto es critico")
    log.warning("Esto es un warning")