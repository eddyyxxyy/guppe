"""
8) Escreva um programa que leia 10 números e escreva o menor
valor lido e o maior valor lido.
"""

print(
    '=' * 29 + '\n' +
    'MENOR E MAIOR DE 10 NÚMEROS'.center(29, '-') + '\n' +
    '=' * 29 + '\n'
)

numbers: list = list()

for i in range(10):
    while True:
        try:
            number = float(
                input(f'Informe o {i + 1}º número:\n->  ')
            )
        except ValueError:
            print('Valor inválido! Tente novamente...\n')
        else:
            numbers.append(number)
            break

print(
    f'Valores: {numbers}'.replace('[', '').replace(']', '') + '\n'
    f'Maior número entre os valores: {max(numbers)}' '\n'
    f'Menor número entre os valores: {min(numbers)}'
)
