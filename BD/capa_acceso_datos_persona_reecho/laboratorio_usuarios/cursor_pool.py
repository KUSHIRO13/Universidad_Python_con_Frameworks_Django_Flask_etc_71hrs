from logger_base import log
from connetion import Connetion

class CursorPool:
    def __init__(self):
        self._cursor = None
        self._connetion = None

    def __enter__(self):
        self._connetion = Connetion.obtained_connetion()
        # log.debug(f"Obtener la conexion {self._connetion}")
        self._cursor = self._connetion.cursor()
        return self._cursor

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_value is not None:
            self._connetion.rollback()
            log.error(f"Ocurrio un error {exception_type} {exception_value} {traceback}")
        else:
            self._connetion.commit()
            # log.info(f"Se realizo commit")
        self._cursor.close()
        Connetion.leave_connetion(self._connetion)

if __name__ == "__main__":
    with CursorPool() as cursor:
        log.debug(f"Inicio del with")
        cursor.execute("SELECT * FROM usuario")
        registro = cursor.fetchall()
        log.debug(registro)
        log.debug(f"FIn del With")