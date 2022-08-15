"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de Classes:


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo separados por Underline para funções e variáveis:


def soma():
    pass


def soma2():
    pass


numero = 4
numero_impar = 5

[3] - Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('Tem')

[4] - Separar funções e definições de classe com 2 linhas em branco, métodos dentro
de uma classe devem ser separados com uma única linha em branco;

[5] - Imports devem ser sempre feitos em linhas separadas:
# Errado:

import sys, os

# Certo:

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote:

from types import (
    StringTypes,
    ListType,
    SetType,
    ...
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentário
# ou DocStrings e antes de constantes ou variáveis globais.

[6] - Não coloque espaço em empressões e instruções:

# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = list [indice]

# Faça:

dict['chave'] = list[indice]

# Não faça:

x                       = 1
y                       = 3
variavel_longa_demais_a = 5

# Faça:

x = 1
y = 1
variavel_longa_demais_a = 5

[7] - Termine sempre uma instrução com uma nova linha:
"""
