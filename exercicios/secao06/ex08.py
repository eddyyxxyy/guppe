"""
8) Escreva um programa que leia 10 números e escreva o menor
valor lido e o maior valor lido.
"""
from locale import atoi
from collections.abc import Iterator


def get_numbers(n: int) -> Iterator[int]:
    for question in range(1, n + 1):
        while True:
            try:
                yield atoi(input(f'{question}º number: ').strip())
                break
            except ValueError:
                print('Invalid number! Try again...')


def main():
    while True:
        try:
            times = atoi(input('How many numbers you want to input?\n->  '))
            break
        except ValueError:
            print('Invalid number! Try again...')
    numbers = tuple(get_numbers(times))
    print(
        f'\nNumbers → {numbers}'
        f'\nMax → {max(numbers)}'
        f'\nMin → {min(numbers)}'
    )


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:
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
"""