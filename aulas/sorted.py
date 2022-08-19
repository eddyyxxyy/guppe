"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que estamos em listas. O sort() só funciona em listas;
podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, o sorted() serve para ordenar elementos.


# Exemplo:

numeros = (6, 1, 8, 2)
# numeros = {6, 1, 8, 2}
# numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

# Não importa se o objeto é qualquer tipo de dado, ele sempre retorna uma lista com os elementos do iterável ordenados


# Adicionando parâmetros ao sorted():

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))
print(sorted(numeros, reverse=True))  # Ordena do maior para o menor


# Podemos utilizar o sorted para coisas mais complexas:

usuarios = [
    {'username': "samuel", 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': "carla", 'tweets': ['Eu amo meu gato']},
    {'username': "jeff", 'tweets': []},
    {'username': "bob123", 'tweets': [], "cor": "amarelo"},
    {'username': "doggo", 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': "gal", 'tweets': [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando pelo username, ordem alfabética invertida
print(sorted(usuarios, key=lambda user: user["username"], reverse=True))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda tweets: len(tweets["tweets"])))


# Ultimo exemplo:

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

print(sorted(musicas, key=lambda musica: musica["tocou"]))  # Ordena da menos tocada até a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))  # Ordena da mais tocada até a menos tocada
"""
