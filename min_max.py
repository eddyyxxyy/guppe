"""
Min e Max

max() → Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]  # Não importa o tipo de dado
tupla = (1, 8, 4, 99, 34, 129)
conjunto = {1, 8, 4, 99, 34, 129}
dic = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(lista))  # Retorna 129
print(max(tupla))  # 129
print(max(set))  # 129
print(max(dic.values()))  # Sem o values retornara a Key que contém o maior valor, no caso f, com o .values() → 129


# Faça um programa que receba dois valores do usuário e mostre o maior:

# n = int(input('Informe o \033[1;31mprimeiro\033[m número: ')),int(input('Informe o \033[1;34msegundo\033[m número: '))
# print(f'O maior número é ', end='')
# if n[0] == max(n):
#     print('\033[1;31m', end='')
# else:
#     print('\033[1;34m', end='')
# print(f'{max(n)}\033[m')

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val2, val1))


min() → Retorna o menor valor em um iterável ou o menor de dois ou mais elemtentos.

# OBS: Age de forma contrária

# Exemplos

lista = [1, 8, 4, 99, 34, 129]  # Não importa o tipo de dado
tupla = (1, 8, 4, 99, 34, 129)
conjunto = {1, 8, 4, 99, 34, 129}
dic = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(lista))  # Retorna 1
print(min(tupla))  # 1
print(min(set))  # 1
print(min(dic.values()))  # Sem o values retornara a Key que contém o menor valor, no caso a, com o .values() → 1


# Faça um programa que receba dois valores do usuário e mostre o menor:

# n = int(input('Informe o \033[1;31mprimeiro\033[m número: ')),int(input('Informe o \033[1;34msegundo\033[m número: '))
# print(f'O menor número é ', end='')
# if n[0] == max(n):
#     print('\033[1;31m', end='')
# else:
#     print('\033[1;34m', end='')
# print(f'{min(n)}\033[m')

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val2, val1))



# Exemplos mais complexos:

nomes = ['Arya', 'Sansa', 'Dora', 'Tim', 'Oliver']

print(max(nomes))  # Pega o nome levando em consideração a ordem do alfabeto → Retorna 'Tim'
print(min(nomes))  # Pega o nome levando em consideração a ordem do alfabeto, ao contário de max() → 'Arya'

print(max(nomes, key=lambda nome: len(nome)))  # Com o lambda, pega o maior nome em extenção → 'Oliver'
print(min(nomes, key=lambda nome: len(nome)))  # Com o lambda, pega o menor nome em extenção → 'Tim'

# Isso ocorre, pois alteramos a key, o comportamento da função.


musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

print(max(musicas, key=lambda tittle: tittle['tocou']))
print(min(musicas, key=lambda tittle: tittle['tocou']))

# Desafio!!! Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda tittle: tittle['tocou'])['titulo'])
print(min(musicas, key=lambda tittle: tittle['tocou'])['titulo'])

# Desafio!!! Como encontrar a música mais tocada e a menos tocada sem usar max/min e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = max
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
"""
