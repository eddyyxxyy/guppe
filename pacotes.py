"""
Pacotes

A diferença entre módulos e pacotes é que:
- Os módulos são apenas UM arquivo python que tem diversas funções para utilizarmos;
- Já os pacotes, são diretórios contendo uma coleção de módulos;

OBS: nas versões 2.x de Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py. Já nas
versões do Python 3.x não é mais obrigatória a utilização deste arquivo, mas normalmente ainda é utilizado para manter
compatibilidade.

# Exemplos:

from geek import geek1, geek2
from geek.university import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(4, 6))
print(geek2.curso)
print(geek2.funcao2())
print(geek3.funcao3())
print(geek4.funcao4())

# Outros exemplos:

from geek.geek1 import funcao1
from geek.university.geek4 import funcao4

print(funcao1(6, 9))
print(funcao4())
"""
