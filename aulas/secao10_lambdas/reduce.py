"""
Reduce

OBS: A partir do Python 3 → função reduce() não é mais integrada, não é mais built-in. Agora temos de importar e
utilizar essa função à partir do módulo 'functools'

Guido Van Rossum: Utilize a função reduce() se você realmente precisa dela. Em 99% das vezes, um loop for é mais legível

Para entender o reduce():

Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

E você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros, a função e o iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2)  # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3)  # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda
    o resultado e isso é repetido até o final.
    .
    .
    .
    Passo n: resn = f(resn, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderíamos ver a função reduce() como:

(funcaon(...(funcao(funcao(funcao(a1, a2), a3), a4), ...), an)

"""

# Como funciona na prática:

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista:

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce precisamos de uma função que receba dois parâmetros:
print(reduce(lambda x, y: x * y, dados))

# Utilizando um loop normal:

res = 1
for n in dados:
    res = res * n

print(res)
