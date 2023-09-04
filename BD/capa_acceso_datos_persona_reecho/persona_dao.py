from logger_base import log
from persona import Persona
from pool_cursor import PoolCursor

class PersonaDAO:
    """
    DAO = Data Access Object
    CRUD = Create Read Update Delete
    """
    _SELECCIONAR = "SELECT * FROM persona"
    _INSERTAR = "INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s, apellido =%s, email = %s WHERE id_persona = %s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona = %s"

    @classmethod
    def seleccionar(cls):
        with PoolCursor() as cursor:
            try:
                cursor.execute(cls._SELECCIONAR)
                registro = cursor.fetchall()
                personas = []
                for r in registro:
                    persona = Persona(r[0],r[1],r[2],r[3])
                    personas.append(persona)
                return personas
            except Exception as e:
                log.error(f"Ocurrio un tipo error '{e}'")

    @classmethod
    def insertar(cls, persona):
        with PoolCursor() as cursor:
            try:
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.info(f"Se afectaron {cursor.rowcount} filas")
            except Exception as e:
                log.error(f"Ocurrio un error tipo '{e}'")

    @classmethod
    def actualizar(cls, persona):
        with PoolCursor() as cursor:
            try:
                valores = (persona.nombre,persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.info(f"Se actualizaron {cursor.rowcount} registros")
            except Exception as e:
                log.error(f"Ocurrio un tipo {e}")

    @classmethod
    def eliminar(cls,persona):
        with PoolCursor() as cursor:
            try:
                valor = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR,valor)
                log.warning(f"Valor eliminado {cursor.rowcount}")
            except Exception as e:
                log.error(f"Ocurrio un error tipo {e}")


if __name__ == "__main__":
    # Insertar
    persona1 = Persona(nombre="Pedro",apellido="Navara",email="pnavara@gmail.com")
    PersonaDAO.insertar(persona1)
    # Actualizar
    # persona2 = Persona(60,"Jorge","Hanma","hjanma@gmail.com")
    # PersonaDAO.actualizar(persona2)
    # Eliminar
    persona3 = Persona(id_persona=70)
    PersonaDAO.eliminar(persona3)
    # Seleccionar
    persona = PersonaDAO.seleccionar()
    for p in persona:
        log.debug(p)
