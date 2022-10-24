"""
Tipos de Dados Mais Precisos

Já vimos no curso diversos tipos de dados:
    - int;
    - float;
    - str;
    - list;
    - set;
    - dict;
    - tuple;
    - etc...

Agora, à partir da versão 3.8 do Python, temos:
    - Literal;
    - Union;
    - Typed Dictionaries;
    - Protocols;


# Literal type:

from typing import Literal


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida: {operacao!r}')


def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida: {operacao!r}')


# calcula_v1('+', 6, 4)
# calcula_v1('-', 10, 2)
# calcula_v1('*', 3, 5)
# print()
calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
calcula_v2('*', 3, 5)



# Union Type
from typing import Union


def soma(num1: int, num2: int) -> str | int:
    resultado: int = num1 + num2
    if resultado > 50:
        return f'O valor {resultado!r} é muito grande.'
    else:
        return resultado



# Final type
from typing import Final, final

NOME: Final = 'Geek'

print(NOME)


@final
class Pessoa:
    pass


class Estudante(Pessoa):
    pass


    @final
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e estagiando...')



# Typed Dictionaries
from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.10.8', atualizacao=2022)
print(geek)

outro = CursoPython(algo='vai', coisa=123)
print(outro)
"""
# Protocols
from typing import Protocol


class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo!r}.')


class Venda:
    titulo: str = 'Oi'


v1 = Venda()
c1 = Curso
c1.titulo = 'Programação em Python'

estudar(c1)
estudar(v1)
