"""
7) Faça um programa que leia 10 inteiros positivos, ignorando não positivos,
e imprima sua média
"""

print(
    '=' * 44 + '\n' +
    'MÉDIA DE 10 NÚMEROS (INTEIROS E POSITIVOS)'.center(44, '-') + '\n' +
    '=' * 44 + '\n'
)

average_numbers: list = list()

for i in range(10):
    while True:
        try:
            number = int(input(f'Informe o {i + 1}º número inteiro positivo:\n'
                               f'->  ').strip())
        except ValueError:
            print('Valor inválido!')
        else:
            if number > 0:
                average_numbers.append(number)
            else:
                pass
            break

print(
    '\nValores:\n'
    f'{average_numbers}\n'.replace('[', '').replace(']', '') +
    f'A média dos valores equivale à {sum(average_numbers) / len(average_numbers):.2f}'
)
