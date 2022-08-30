"""
5) Faça um programa que peça ao usuário para digitar
10 valores e some-os.
"""

print(
    '=' * 20 + '\n' +
    'SOMA DE 10 NÚMEROS'.center(20, '-') + '\n' +
    '=' * 20 + '\n'
)

sum_numbers: list = list()

for question in range(1, 11):
    while True:
        try:
            print(f'Informe o {question}º número: ')
            asnwer = float(input('->  ').strip().replace(',', '.'))
        except ValueError:
            print('Valor inválido! Tente novamente...\n')
            continue
        else:
            sum_numbers.append(asnwer)
            break

print(
    '\nNúmeros informados:\n'
    f'{sum_numbers}\n'.replace('[', '').replace(']', '') +
    f'\nA soma dos números acima equivale à {sum(sum_numbers)}.'
)
