class calculadora:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

    @property
    def protegido(self):
        return self._protegido

    @protegido.setter
    def protegido(self, protegido):
        self._protegido = protegido

objeto = calculadora('Valor Publico','Valor Protegido','Valor Privado',)

# Publico
print(objeto.publico)
objeto.publico = 'Publico'
print(objeto.publico)


print(objeto._calculadora__privado)