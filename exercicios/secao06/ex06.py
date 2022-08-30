"""
6) Faça um programa que leia 10 inteiros e imprima sua média.
"""

print(
    '=' * 22 + '\n' +
    'MÉDIA DE 10 INTEIROS'.center(22, '-') + '\n' +
    '=' * 22 + '\n'
)

average_numbers: list = list()

for i in range(10):
    while True:
        try:
            number = int(input(f'Informe o {i + 1}º número:\n->  ').strip())
        except ValueError:
            print('Valor inválido! Informe somente números inteiros...\n')
            continue
        else:
            average_numbers.append(number)
            break

print(
    f'\nValores: {average_numbers}\n'.replace('[', '').replace(']', '') +
    f'A média dos valores: {sum(average_numbers) / len(average_numbers)}'
)
