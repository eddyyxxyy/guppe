"""
Chegagem de Tipos de Dados com MyPy

É só rodar o comando mypy e o nome do arquivo,
então ele irá apontar os erros relacionados à
Type Hinting.
"""


def cumprimento(name: str) -> str:
    return name


cumprimento(123)
