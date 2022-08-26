"""
1) Faça um programa que receba dois números e mostre qual deles é o maior.
"""
n1 = float(input('Informe um número: ').strip().replace(',', '.'))
n2 = float(input('Informe outro número: ').strip().replace(',', '.'))
if n1 > n2:
    print(f'O primeiro número, {n1}, é maior que o segundo número {n2}.')
else:
    print(f'O segundo número, {n2}, é maior que o primeiro número {n1}.')
