from cursor_pool import CursorPool
from logger_base import log
from user import User


class UserDAO:
    _SELECT = "SELECT * FROM usuario"
    _SEARCH = "SELECT * FROM usuario WHERE username = %s AND password = %s"
    _INSERT = "INSERT INTO usuario(username,password) VALUES(%s,%s)"
    _UPDATE = "UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s"
    _DELETE = "DELETE FROM usuario WHERE id_usuario = %s"

    @classmethod
    def select(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECT)
            registro = cursor.fetchall()
            usuarios = []
            for r in registro:
                usuario = User(r[0],r[1],r[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insert(cls, user):
        with CursorPool() as cursor:
            valores = (user.username,user.password)
            cursor.execute(cls._INSERT,valores)
            log.info(f"Se inserto {cursor.rowcount} registro")

    @classmethod
    def update(cls, user):
        with CursorPool() as cursor:
            valores = (user.username, user.password, user.id_usuario)
            cursor.execute(cls._UPDATE,valores)
            log.warning(f"Se actualizo {cursor.rowcount} registro")

    @classmethod
    def delete(cls, user):
        with CursorPool() as cursor:
            valor = (user.id_usuario,)
            cursor.execute(cls._DELETE,valor)
            log.warning(f"Se elimino {cursor.rowcount} registro")

    @classmethod
    def search(cls, user):
        with CursorPool() as cursor:
            valor = (user[0], user[1])
            cursor.execute(cls._SEARCH,valor)
            registro = cursor.fetchall()
            busqueda = []
            for r in registro:
                usuarios = User(r[0],r[1],r[2])
                busqueda.append(usuarios)
            return busqueda

if __name__ == "__main__":
    # Delete
    # user3 = User(3)
    # UserDAO.delete(user3)
    # Update
    # user2 = User(3, "Luis", "XXXLUISXXX")
    # UserDAO.update(user2)
    # Insertar
    user1 = User(username="Rouse", password="Rochi")
    UserDAO.insert(user1)
    # Seleccionar
    usuarios = UserDAO.select()
    for u in usuarios:
        log.debug(u)
    user4 = ["Rouse","Rochi"]
    usuario = UserDAO.search(user4)
    for u in usuario:
        log.debug(u)