"""
Annotations

As Annotations são as Type Hints, simples assim.

# Exemplos:

import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


# print(circunferencia.__annotations__)
# # {'raio': <class 'float'>, 'return': <class 'float'>}
#
# nome: str = 'Edson Pimenta'
# peso: float = 65.5
# ativo: bool = True
#
# print(nome)
# print(peso)
# print(ativo)
#
# print(__annotations__)
# # {'nome': <class 'str'>, 'peso': <class 'float'>, 'ativo': <class 'bool'>}


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self._nome: str = nome
        self._idade: int = idade
        self._peso: float = peso

    def andar(self) -> str:
        return f'{self._nome} está andando...'


p = Pessoa('Edson Pimenta', 22, 65.5)
# print(p.__annotations__)  # A instância não possui annotations
print(p.__dict__)
print(p.andar.__annotations__)
print(p.__init__.__annotations__)
"""
