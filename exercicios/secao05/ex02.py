"""
2) Leia um número fornecido pelo usuário. Se esse númerro for positivo,
calcule a raiz quadrada do número. Se o número for negativo, mostre
uma mensagem dizendo que o número é inválido.
"""
from math import sqrt

n = float(input('Informe um número: ').strip().replace(',', '.'))
if n == 0:
    print(f'O número 0 é neutro.')
elif n > 0:
    print(f'A raiz quadrada do número {n} é {sqrt(n)}.')
else:
    print(f'O número {n} é inválido.')
