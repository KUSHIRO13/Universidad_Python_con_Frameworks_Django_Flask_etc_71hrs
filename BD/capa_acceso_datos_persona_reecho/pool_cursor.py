from connetion import Connetion
from logger_base import log


# Creación de la clase cursor del pool
class PoolCursor:
    def __init__(self):
        self._connetion = None
        self._cursor = None
# El dunder enter se inicia al utilizar el método with
    def __enter__(self):
        log.info("Se inicia el WITH con ENTER")
        self._connetion = Connetion.obtained_connetion()
        self._cursor = self._connetion.cursor()
        return self._cursor

# El dunder exit se inicia cuando se lee la última línea dentro de un método with
# Los atributos exception_type, exception_value y el traceback_exception hacen referencia a
# El tipo de excepción, el valor de la excepción y al rastreo del detalle o excepción
    def __exit__(self, exception_type, exception_value, traceback_exception):
        log.info("Se ejecuta el metodo __exit__")
        if exception_value is not None:
            self._connetion.rollback()
            log.error(f"Ocurrio un error '{exception_value}'\nTipo: {exception_type}\nDetalle: {traceback_exception}")
        else:
            self._connetion.commit()
            log.debug("Commit de la transaccion")
        self._cursor.close()
        Connetion.leave_connetion(self._connetion)

if __name__ == "__main__":
    with PoolCursor() as cursor:
        log.debug(f"Dentro del with")
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())