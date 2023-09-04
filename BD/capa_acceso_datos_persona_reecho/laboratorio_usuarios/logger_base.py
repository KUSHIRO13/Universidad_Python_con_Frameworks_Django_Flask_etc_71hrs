import logging

log = logging
log.basicConfig(level=log.DEBUG,
                format="%(asctime)s [%(levelname)s](%(filename)s-%(lineno)s): %(message)s",
                datefmt="%I:%M %p",
                handlers=[
                    log.FileHandler("file.log"),
                    log.StreamHandler()
                ])

if __name__ == "__main__":
    log.info(f"Esto es un INFO")