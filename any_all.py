"""
Any e All

all() → retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vázio.
# Exemplo:

print(all([0, 1, 2, 3, 4]))  # Todos os elementos são verdadeiros? → retorna False, por causa do valor 0
print(all([1, 2, 3, 4]))  # Retorna True
print(all([]))  # Retorna True
print(all(''))  # Retorna True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))  # Todos os elementos começam com 'C', então retorna True

print(all([letra for letra in 'eio' if letra in 'fjp']))
# OBS: Retorna True mesmo assim, pois diferente da classe booleana, o all considera conjuntos vazios como True.

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
# OBS: mesmo que mudemos a condição para detectar números ímpares, daria True, pois o all considera conjuntos vazios
# como True.

any() → Retorna True se qualquer elemento do elemento for verdadeiro, se o iterável estiver vazio, retorna False.
# Exemplo:

print(any([0, 1, 2, 3, 4]))  # Se pelo menos um dos elementos for True, ele retorna True.
print(any([0, False, {}, (), []]))  # Como todos são False, ele retorna False.

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))  # Se fosse o all(), retornaria False, pois um dos elementos não começa
# com 'C'

print(any([num for num in [4, 2, 6, 10, 8, 9] if num % 2 == 0]))  # Há pelo menos um True, um par, retorna True
print(any([num for num in [4, 2, 6, 10, 8] if num % 2 != 0]))  # Não há ímpares, retorna False
"""
