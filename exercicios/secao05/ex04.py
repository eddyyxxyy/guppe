"""
4) Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado
    - A raiz quadrada ao número digitado
"""
from math import sqrt

n = float(input('Informe um número: ').strip().replace(',', '.'))
if n == 0:
    print('O número 0 ao quadrado resulta em 0 e sua raiz quadrada também.')
elif n > 0:
    print(
        f'O quadrado de {n} corresponde à {n ** 2};\n'
        f'A raiz quadrada de {n} é {sqrt(n)}'
    )
else:
    print(f'{n} é negativo.')
