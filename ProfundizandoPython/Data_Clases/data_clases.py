from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(frozen=True)
class Persona:
    nombre: str
    apellido: str
    contador_persona: ClassVar[int] = 0
    domicilio: Domicilio

    def __post_init__(self):
        if self.nombre == '':
            raise ValueError(f"Valor de nombre vacio")
        if self.apellido == '':
            raise ValueError(f"Valor de apellido vacio")
if __name__ == '__main__':
    domicilio1 = Domicilio('Saturno', 15)
    persona1 = Persona('Juan', 'Perez', domicilio1)
    print(persona1)
    print(persona1.contador_persona)
    persona_vacia = Persona('Andres','Cortina', Domicilio("Alpes", 1652))
    print(persona_vacia)

    # Revisar igualdad
    persona2 = persona1
    print(f'Objectos iguales {persona1 is persona2}')
    colecion = {persona1, persona2, persona_vacia}
    print(colecion)
