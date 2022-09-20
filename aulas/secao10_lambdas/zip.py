"""
Zip

zip() → Cria um iterável (Zip Object) que agrega o elemento de cada um dos iteráveis passados como entrada em pares.

# Exemplos:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, set ou dicionário:

zip1 = zip(lista1, lista2)
print(list(zip1))  # Gerou uma lista com tuplas com pares entre o 1 elemento de cada lista. Formando pares nas tuplas.

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

# No dicionários, os pares se tornam chave: valor, os elementos da primeira lista informada se tornam as chaves e os
# valores da segunda lista se tornam os valores.
zip1 = zip(lista1, lista2)
print(dict(zip1))


# O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver trabalhand ocom iteráveis
# de tamanho diferentes, o método irá parar quando os elementos do menor iterável acabarem. Não importando a ordem de
# declaração dos argumentos.
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas:

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))


# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utilizar o map para isso

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
"""
