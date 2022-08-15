"""
Trabalhando com módulos Built-in (Módulos integrados, que já vem com o Python nativo)

Para que não sobrecarregue o uso de memória do Python, os módulos que já vem instalados no python (Built-ins), ficam
a disposição para o import, assim mantendo otimizada a codificação.


# Utilizando alias (apelidos) para módulos/funções

import random as rdm

print(rdm.random())



from random import randint as rdi

print(rdi(5, 89))



# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())
print(shuffle(['Batata', 'Maçã', 'Cenoura']))


# Importando tod0 o módulo:

import random

print(random.random())


# Costumamos a utilizar tupple para colocar multiplos imports de um mesmo módulo:

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(1, 6))
lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)
print(choice('University'))

"""
