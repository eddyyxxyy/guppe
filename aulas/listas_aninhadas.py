"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (por exemplo, C/Java/PHP) possuem uma estrutura de dados chamadas de arrays:
    - Unidimencionais (Arrays/Vetores)
    - Multidimencionais (Matrizes)

Em Python nós temos as listas:

numero = [1, 2, 3, 4, 5] → Em Python são listas, em outras linguanges são Arrays/Vetores.
OBS: Em outras linguagens, quando definimos um Array/Vetor, eles tem tamanho fixo e só podem ter um tipo de dado. Já em
Python podemos misturar dados e o limite de tamanho dele é dinâmico, mutável.


# Exemplos:

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3 (3 linhas x 3 colunas), Array Multidencional em outras lings.

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1])  # 2
print(listas[2][1])  # 8
print(listas[2][-2])  # 8

# Como fazemos para iterar com loops em uma lista aninhada?

for lista in listas:
    for valor in lista:
        print(valor, end=' ')
        if valor % 3 == 0:
            print('')

# Com List Comprehension:

[[print(valor, end=' ') for valor in lista] for lista in listas]

"""

# Outros Exemplos

# Gerando um tabuleiro/matriz 3x3:

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha:

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais:

print([['*' for i in range(1, 4)] for j in range(1, 4)])
