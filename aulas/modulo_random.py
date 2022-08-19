"""
Módulo Random e o que são módulos?

Em Python, módulos nada mais são do que: outros arquivos Python, todos os arquivos que fiz até agora são módulos.
Os modulos são uteis para que possamos deixar nossos programas mais simples e para que possamos reutilizar códigos.

Módulo Random → Possui varias funções para geração de números pseudo-aleatórios.
pseudo-aleatório → Só não é completamente aleatório, pois pode haver repetição.

# OBS: existem duas formas de se utilizar um módulo ou função deste.



# Forma 1 - Importando tod0 o módulo

import random


# Ao realizar o import de tod0 o módulo, todas as funções, atributos, classes e propriedades que estiverem dentro do
# módulo ficarão disponíveis (em memória, pronto para utilização).

# NÃO RECOMENDADO, caso você saiba quais funções você precisa utilizar deste módulo, então esta não seria a forma ideal
# de utilização. Verifique a forma 2.


print(random.random())

# random() gera um número pseudo-aleatório entre 0 e 1.

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função
# separados por "."

# Não confunda a função random() com o pacote random, apesar de terem o mesmo nome, sabemos que random() é uma
# função pois abre e fecha parênteses. Pode parecer confuso, mas a função random() é apenas uma função dentro
# do módulo random


# Forma 2 - Importando uma função específica do módulo:

from random import (random)

# No import acima estamos falando: do módulo random importe a função random

for i in range(10):
    print(random())

# A forma exposta acima, é a RECOMENDADA



# uniform() → Gerar números pseudo-aleatórios entre os valores estabelecidos:

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # O 7 não é incluído, o valor final sempre é n-1, terminará no 6

# Na função gera um número real pseudo-aleatório entre 3 e menor que 7



# randint() → gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.

# Gerador de apostas para a Mega-Sena:

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')  # Começa em 1 e termina em 61-1, ou seja, 60, gera números entre 1 e 60



# choice() → Mostra um valor aleatório entre um interável:

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

print(choice('Geek University'))



# shuffle() → Tem a função de embaralhar dados:

from random import shuffle

cartas = ['K', 'J', 'Q', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas.pop())


# Imagine que se não existissem esses módulos/pacotes, iriamos acabar tendo de resolver milhares de problemas para
# realizar as mesmas tarefas que fazemos com facilidade utilizando os módulos.
"""
