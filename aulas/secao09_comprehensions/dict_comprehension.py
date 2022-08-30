"""
Dictionary Comprehension

Se quisermos criar uma lista, fazemos:

lista = [1, 2, 3, 4]

Se quisermos uma tupla:

tupla = (1, 2, 3, 4)
ou:
tupla = 1, 2, 3, 4

Se quisermos um set (conjunto):

set = {1, 2, 3, 4}

Se quisermos um dict (dicionário):

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

OBS: O mais diferente entre eles é o dicionário, pois temos um conjunto de chave/valor (key/value), se parecendo com o
set, porém o set não tem chave.

# Syntax do Dictionary Comprehension

{chave:valor for valor in iterável}

# Comparando com o list comprehension seria:

[valor for valor in iterável]


# Exemplos:

# 1

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

# 2

numeros = [1, 2, 3, 4]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

# 3

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

misturado = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(misturado)


# Exemplos com lógica condicional:

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)
"""
