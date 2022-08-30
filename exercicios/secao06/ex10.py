"""
10) Faça um programa que calcule e mostre a soma dos 50
primeiros números pares.
"""

print(
    '=' * 34 + '\n' +
    'SOMA DOS 50 PRIMEIROS PARES'.center(34, '-') + '\n' +
    '=' * 34 + '\n'
)

sum_number: int = 0

for number in range(2, 51, 2):
    sum_number += number

print(f'A soma dos valores equivale à: {sum_number}')