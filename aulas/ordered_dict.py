"""
Ordered Dict → Dicionário Ordenado
Módulo Collections
High-performance Container Datatypes

# Em um dicionário, a ordem de inserção dos elementos não é garantida,
mesmo que ele informe corretamente a ordem como foi informada, isso pode mudar.

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'Chave = {chave}:Valor = {valor}')

# Entendendo a diferença entre dict e Ordered Dict:

Em dicionários comuns, a ordem dos elementos não importa, um dicionário que declara os mesmos valores
que outro são reconhecidos como a mesma coisa. Se os dicionários forem Ordered, eles só vão reconhecer
dois dicionários como iguais se tiverem os mesmos elementos na mesma ordem.
"""

