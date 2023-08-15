from conexion import Conexion
from logger_base import log
from persona import Persona


class PersonaDAO:
    """
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    """
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona ASC"
    _INSERTAR = "INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s,apellido =%s,email = %s WHERE id_persona = %s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona =%s"

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f"Persona a insertar {persona}")
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f"Persona actualizada: {persona}")
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.id_persona)
                cursor.execute(cls._ELIMINAR,(valores,))
                log.warning(f"Personas eliminados {persona}")
                return cursor.rowcount


if __name__ == "__main__":
    # Insertar
    persona1 = Persona(nombre="Pedro",apellido="Najera",email="pnajera@gmail.com")
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f"Personas insertadas: {personas_insertadas}")

    # Actualizar
    persona1 = Persona(52,"Kevin", "Pinzon", "kpinzon@gmail.com")
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f"Personas actualizadas: {personas_actualizadas}")

    # Eliminar
    persona1 = Persona(id_persona=55)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.warning(f"Personas eliminadas: {personas_eliminadas}")

    # Seleccionar
    persona = PersonaDAO.seleccionar()
    for personas in persona:
        log.debug(personas)
