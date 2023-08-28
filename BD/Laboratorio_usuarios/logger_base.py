import logging as log

log.basicConfig(level=log.DEBUG,
                format="[%(levelname)s] %(asctime)s: (%(filename)s-%(lineno)s) %(message)s",
                datefmt="%I:%M %p",
                handlers=[
                    log.FileHandler("info.log"),
                    log.StreamHandler()
                ])

if __name__ == "__main__":
    log.debug(f"Esto es un DEBUG")