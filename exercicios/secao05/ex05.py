"""
5) Faça um programa que receba um número inteiro e verifique se este número é
par ou ímpar.
"""
n = round(float(input('Informe um número inteiro: ').strip().replace(',', '.')))
if n == 0:
    print('O número 0 é neutro.')
elif n % 2 == 0:
    print(f'{n} é par!')
else:
    print(f'{n} é ímpar!')
