"""
Filter

filter() → Serve para filtrar dados de uma determinada coleção.

Exemplos:

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

# OBS: Assim como a função map(), a filter(), recebe dois parâmetros, sendo
# uma função e um iterável.

# res = filter(lambda x: x > media, dados)  # pode ser feito assim.
# print(list(res))

# ou podemos:
print(list(filter(lambda x: x > statistics.mean(dados), dados)))

# OBS: assim como na função map(), após serem utilizados os dados de filter(),
# eles são excluídos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)
# Ou: res = filter(lambda pais: len(pais) > 0, paises)  # Porém assim é pior
# Ou: res = filter(lambda pais: pais != '', paises)

print(list(res))


# A diferença entre map() e filter() é:
# A map(), recebemos 2 parâmetros, uma função e um iterável e isso retorna um objeto mapeando a função para cada
# elemtento do iterável.
# O filter() recebe 2 parâmetros, uma função e um iterável e retorna um objeto com apenas os elementos de acordo com
# o filtro aplicado.


# Exemplo mais complexo:

usuarios = [
    {'username': "samuel", 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': "carla", 'tweets': ['Eu amo meu gato']},
    {'username': "jeff", 'tweets': []},
    {'username': "bob123", 'tweets': []},
    {'username': "doggo", 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': "gal", 'tweets': []}
]

# Filtrar os usuários que estão inativos no Twitter:
# inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))
inativos = list(filter(lambda user: not user['tweets'], usuarios))
print(inativos)


# Como combinar filter() e map():

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo sua instrutora é + o nome da instrutora desde que cada nome tenha menos de 5 carac-
# teres

lista = list(map(lambda nome: f'Sua instrutura é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

"""
