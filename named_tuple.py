"""
Named Tuple → Tupla Nomeada
Módulo Collections
High-performance Container Datatypes

Recap tuplas:

tupla = (1, 2, 3)

print(tupla[1])

Named Tuple → São tuplas diferenciadas, onde especificamos para a mesma e também parâmetros.

Exemplo:

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros:

# Forma 1:

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2:

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3:

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Utilizando

ray = cachorro(idade=2, raca='Chow Chow', nome='Ray')

# Acessando os dados

# Forma 1:

print(ray)
print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

# Forma 2:

print(ray.idade)
print(ray.raca)
print(ray.nome)

# Lembrando que podemos fazer o mesmo que já faziamos com tuplas antes:

print(ray.index('Chow Chow'))
print(ray.count('Chow Chow'))
"""

