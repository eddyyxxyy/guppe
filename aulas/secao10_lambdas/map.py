"""
Map

Com map, fazemos mapeamento de valores para função.


import math


def area(r):
    # Calcula a área de um círculo com raio 'r'.  # Era pra ser uma docstring, para deixar aqui mudei para '#'
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum:

areas = []
for r in raios:
    areas.append((area(r)))

for areass in areas:
    print(f'{areass:.2f},', end=' ')

# Forma 2 (utilizando map):

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 (utiliando lambda e map):

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map(), depois da primeira utilização resultado, ele zera.
# só podemos utilizá-la uma vez, ela limpa a memória depois de usada.


# Para fixar - Map

# Temos dados interáveis:

# dados: a1, a2, a3..., an

# Temos uma função:

# Função f(x)

# Utilizamos a função map(f, dados) onde map irá mapear cada elemento de 'dados' e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an)
"""

# Mais um exemplo:

cidades = [
    ('Berlin', 29),
    ('Cairo', 36),
    ('Buenos Aires', 19),
    ('Los Angeles', 26),
    ('Tokio', 27),
    ('Nova York', 28),
    ('Londres', 22),
]

print(cidades)

# Para converter para Fahrenheit: f = 9 / 5 * c + 32

# Lambda para isso:

print(
    list(map(lambda dado: (dado[0], round((9 / 5) * dado[1] + 32)), cidades))
)

"""
Estamo mandando imprimir um map convertido para uma lista (assim sendo possível visualizar os dados contidos no objeto
map), primeiro (após declarar lambda) definimos qual o parâmetro de entrada da função (que é o dado que será puxado de
cada elemento da lista cidades nesse exemplo), então definimos que o dado[0] de cada elemento (que resulta no nome de
cada cidade) será mantido e que o dado[1] (que é a temperatura) será convertido usando os calculos para se tornar
fahrenheit, após isso informamos qual o iterável, a lista cidades, que terá cada um dos seus elementos mapeados e
executados pela função lambda, cada elemento será o 'dado'.
OBS: o round() serve para arredondar os valores.
"""
