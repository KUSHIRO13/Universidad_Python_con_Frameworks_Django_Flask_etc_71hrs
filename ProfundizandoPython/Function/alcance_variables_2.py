# Mas de alcande de variables
def funcion_externa():
    var_local_externa = 'Variable Local Externa'
    def funcion_anidada():
        var_local_anidada = 'Variable Local Anidada'
        nonlocal var_local_externa
        var_local_externa = 'Nuevo Valor'
        print(f"Nuevo valor : {var_local_externa}")

    funcion_anidada()

    
funcion_externa()
