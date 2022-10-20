"""
Operador Walrus

À partir da versão 3.8, o Python teve
implementado o Operador Walrus.

O Walrus é um operador que permite fazer
a atribuição e retorno de valor em uma
única expressão.

Syntax:

variavel := expressão


# Forma padrão
nome: str = 'Edson Pimenta'
print(nome)

# Com Walrus
print(nome := 'Isabela Gavilan')
print(nome)


# Até Python 3.7, padrão:
cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')

# Python 3.8, lesgooo:
cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)
"""
