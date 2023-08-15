from logger_base import log
class Persona:
    def __init__(self, id_persona=None, nombre="NULL", apellido="NULL", email="NULL"):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f"""
\tId Persona: {self._id_persona}
\tNombre: {self._nombre}   Apellido: {self._apellido}
\tGmail: {self._email}"""

    @property
    def id_persona(self):
        return self._id_persona
    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    @property
    def email(self):
        return self._email

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    @email.setter
    def email(self, email):
        self._email = email


if __name__ == "__main__":
    persona1 = Persona(1,"Andres", "Lara", "alara@gmail.com")
    log.debug(persona1)
    # Simular un INSERT
    persona1 = Persona(nombre="Carlos",apellido="Gutierres",email="cgutierres@gmail.com")
    log.debug(persona1)
    # Simular un DELETE
    persona1 = Persona(id_persona=1)
    log.warning(persona1)
