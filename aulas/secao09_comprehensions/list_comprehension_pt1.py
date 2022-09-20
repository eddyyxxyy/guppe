"""
List Comprehension - Parte I

- Utilizando List Comprehension, nós podemos gerar novas listas com dados processados a partir de outro interável.

# Syntax da List Comprehension:

[ dado for dado in iterável ]


# Exemplos:

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


Logo: estamos criando uma lista que, para cada dado na lista numeros, multiplicamos o valor em 10, criando uma lista
com os valores da lista multiplicados por 10, iterando sobre cada valor da lista formando uma nova. Isso é List Compre-
hension.


numeros = [1, 2, 3, 4, 5]

res = [numero / 2 for numero in numeros]

print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]

print(res)


# List Comprehension x Loop

# Loop:

numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

# List Comprehension:

print([numero * 2 for numero in [1, 2, 3, 4, 5]])


# Outros exemplos:

# 1

nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.title() for amigo in amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])
"""
