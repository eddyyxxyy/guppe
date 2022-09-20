"""
Default Dict → Dicionário Padrão
Módulo Collections
High-performance Container Datatypes → Containers para alta performance

Recap (dicionários):

dicionario = {'curso': 'Programação em Python Essencial'}

print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # KeyError → pois a chave não existe

Ao criar um dicionário utilizando o Default Dict nós informamos um valor Default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não
houver um valor definido. Caso tentemos acessar uma chave que não existe, essa
chave será criada e o valor Default será atribuído à essa chave.

OBS: Lambdas são funções sem nome que podem ou não receber parametros de entrada e retornar valores.

Exemplo:

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação Python Essencal'

print(dicionario)

print(dicionario['outro'])  # se fosse um dicionário comum daria KeyError

print(dicionario)
"""
