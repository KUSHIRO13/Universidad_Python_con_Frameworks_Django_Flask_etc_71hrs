import logging

log = logging

log.basicConfig(
    level=log.DEBUG,
    format="[%(levelname)s]-%(asctime)s: %(filename)s-%(lineno)s: %(message)s",
    datefmt="%I:%M %p",
    handlers=[
        log.FileHandler("Ultima_prueba.log"),
        log.StreamHandler()
    ]
)

if __name__ == "__main__":
    log.debug("Esto seria el DEBUG")
    log.info("Esto seria el INFO")
    log.error("Esto seria el ERROR")
    log.critical("Esto seria el CRITICAL")
    log.warning("Esto seria el WARNING")