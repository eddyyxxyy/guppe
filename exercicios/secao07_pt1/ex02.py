"""
2) Crie um programa que lê 6 valores inteiros e, em seguida,
mostre na tela os valores lidos
"""
numeros: list = []
for numero in range(6):
    numeros.append(int(input('Informe um número inteiro: ')))
print(numeros)
