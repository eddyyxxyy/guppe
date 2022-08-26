"""
12) Ler um número inteiro. Se o número lido for negativo, escreva a mensagem
'Número inválido'. Se o número for positivo, calcular o logaritmo deste número.
"""
from math import log10

n = str(input('Informe um número inteiro positivo: ').strip().replace(',', '.'))
try:
    int(n)
except ValueError:
    print(f'"{n}" é inválido!')
    exit()
else:
    print(f'O logaritmo de {n} na base 10 é: {log10(int(n))}')
