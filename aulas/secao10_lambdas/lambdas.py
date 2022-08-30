"""
Utilizando Lampdas

Conhecidas por Expressões Lambdas ou simplesmente Lambdas, são funções sem nome,
ou seja, funções anônimas.


# Função em Python:


def funcao(x):
    return x * 3 + 1


print(funcao(4))
print(funcao(7))


# Expressão Lambda:

lambda x: x * 3 + 1

# E como utilizar a expressão Lambda?

calc = lambda x: x * 3 + 1

print(calc(4))
print(calc(7))


# Podemos ter expressões Lambdas com multiplas entradas:

nome_completo = lambda nome, sobrenome: nome.strip().title() +  ' ' + sobrenome.strip().title()

print(nome_completo('    angelina ', 'JOLIE  '))
print(nome_completo('    FELICITY                ', '  jones    '))

OBS: Podemos ter expressões lambdas sem nenhum parâmetro de entrada. E lembrando que, se passarmos mais parâmetros do
que os esperados, teremos TypeError.


# Um bom exemplo de uso de lambdas:

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

"""

# Função quadrática:
# f(x) = a * x ** 2 + b * x + c

# Definindo a função:


def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))
