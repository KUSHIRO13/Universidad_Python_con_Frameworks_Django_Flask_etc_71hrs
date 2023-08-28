import logging

log = logging

log.basicConfig(level=log.DEBUG,
                format="[%(levelname)s] %(asctime)s: %(filename)s-%(lineno)s %(message)s",
                datefmt="%I:%M %p",
                handlers=[
                    log.FileHandler("info1.log"),
                    log.StreamHandler()
                ])

if __name__ == "__main__":
    log.info("Esto es un INFO")

