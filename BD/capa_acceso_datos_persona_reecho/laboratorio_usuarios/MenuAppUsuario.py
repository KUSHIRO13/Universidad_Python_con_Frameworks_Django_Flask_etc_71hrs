from cursor_pool import CursorPool
from user import User
from userDAO import UserDAO

if __name__ == "__main__":
    # Variables
    opciones, usuarios, username, password = None, None, None, None

    # Inicio Bucle
    while opciones != "5":
        opciones = input("""Opciones:
1) Listar Usuarios
2) Agregar Usuario
3) Modificar Usuario
4) Eliminar Usuario
5) Salir
>>: """)
        if opciones == "1":
            usuarios = UserDAO.select()
            for user in usuarios:
                print(user)
        elif opciones == "2":
            with CursorPool() as cursor:
                username = input("Ingrese su nombre de usuario: ")
                password = input("Ingrese su contraseña: ")
                usuarios = User(username=username, password=password)
                UserDAO.insert(usuarios)
        elif opciones == "3":
            with CursorPool() as cursor:
                confirmacion = [input("Como se llama el usuario?: "), input("Cual es la contraseña?: ")]
                busqueda = UserDAO.search(confirmacion)
                if len(busqueda) > 0:
                    for b in busqueda:
                        print(b)
                    print("El usuario a modificar es uno de estos?")
                    si_no = input("1) Si\n2) No\n>>: ")
                    if si_no == "1":
                        actualizar = input("Entonces cual es su id: ")
                        nombre = input("Cual sera el nuevo nombre: ")
                        contrasena = input("Cual sera la nueva contraseña: ")
                        usuarios = User(actualizar, nombre, contrasena)
                        UserDAO.update(usuarios)
                    else:
                        print("Tal vez se equivoco de opcion")
                else:
                    print(
                        f"No se encontraron resultados para '{confirmacion[0]}' con la contraseña '{confirmacion[1]}'")
        elif opciones == "4":
            confirmacion = [input("Como se llama el usuario?: "), input("Cual es la contraseña?: ")]
            usuarios = UserDAO.search(confirmacion)
            if len(usuarios) > 0:
                for u in usuarios:
                    print(u)
                print("El usuario es uno de estos?")
                si_no = input("1) Si\n2) No\n>>: ")
                if si_no == "1":
                    eliminar = input("Cual es el id de la persona a eliminar: ")
                    usuario = User(eliminar)
                    UserDAO.delete(usuario)
                else:
                    print("Tal vez se equivoco de numero")
            else:
                print(f"No se encontraron resultados para '{confirmacion[0]}' con la contraseña '{confirmacion[1]}'")
        elif opciones == "5":
            print("Vuelva pronto")
