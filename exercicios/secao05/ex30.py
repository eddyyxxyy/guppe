"""
30) Faça um programa que receba três números e mostre-o em ordem crescente.
"""
from collections import deque

print('-=' * 15 + '\n' + 'NÚMEROS EM ORDEM CRESCENTE'.center(30, '-') + '\n' + '=-' * 15)
numbers: deque = deque()
for i in range(3):
    while True:
        try:
            numbers.append(float(input(f'Informe o {i}º número: ').strip().replace(',', '.')))
        except ValueError:
            print(f'Valor inválido!')
            continue
        else:
            break
print(f'Os números em ordem crescente: {sorted(numbers)}')
