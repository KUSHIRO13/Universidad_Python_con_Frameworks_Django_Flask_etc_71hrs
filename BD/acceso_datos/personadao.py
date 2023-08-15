from conexion import Conexion as cn
class PersonaDao:
    SELECCIONAR = "SELECT * FROM persona"
    INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)"

    @classmethod
    def seleccionar(cls, cursor):
        c = cursor
        c.execute(cls.SELECCIONAR)
        registro = cursor.fetchall()
        return registro

    @classmethod
    def insertar(cls, cursor, nombre, apellido, email):
        sentencia = cls.INSERTAR
        cursor.execute(sentencia, (nombre, apellido, email))




if __name__ == "__main__":
    # Prueba de conexion
    conexion = cn.obtenerConnexion()
    print(conexion)
    cursor = cn.obtenerCursor()
    print(PersonaDao.seleccionar(cursor))

    # Prueba insercion
    PersonaDao.insertar(cursor,"Andres", "Cortina", "acortina@gmail.com")
    print(cn.cerrar(conexion,cursor))