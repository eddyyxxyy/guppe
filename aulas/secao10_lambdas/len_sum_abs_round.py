"""
Len, Abs, Sum e Round

# Len:

len() → Retorna o tamanho, ou seja, o número de items de um iterável

# Exemplo:

print(len('Geek University'))
print(len([1, 2, 3, 4, 5, 6]))
print(len((1, 2, 3, 4, 5, 6)))
print(len({1, 2, 3, 4, 5, 6}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}))
print(len(range(0, 10)))

# Por debaixo dos panos, o Python faz o seguinte:

# Dunder ('__') len → __len__
print('Geek University'.__len__())


# Abs:

abs() → Retorna o valor absoluto de um número, inteiro ou real, de forma básica seria o seu valor real sem o sinal.

# Exemplo:

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Retorna tudo positivo, se o número for negativo ele tira o sinal, se for positivo ele simplesmente mostra o número.

# Não podemos utilizar o abs() numa string


# Sum:

sum() → Recebe como parâmetro como interável, podendo receber um valor inicial, e retorna a soma total dos elementos
incluindo o valor inicial

# OBS: O valor inicial default é 0

# Exemplos:

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], -5))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([3.145, 5.678]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b':2, 'c': 3, 'd': 4, 'e': 5}.values()))

# OBS: Não conseguimos usar o sum() em Strings, pois o valor default é 0, então a soma não ocorre, porém podemos usar
# o join


# Round:

round() → Retorna um número arredondado para o n digito de precisão após a casa decimal, se a precisão não for informada
retorna o inteiro mais próximo da entrada

# Exemplos:

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2121212121, 2))
print(round(1.21999999, 2))

# Até n.5 ele arredonda para baixo, após isso ele arredondará para cima.
# Caso queiramos um valor inteiro, é só não informar o valor de precisão.
"""
