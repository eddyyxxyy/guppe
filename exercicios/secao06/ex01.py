"""
1) Faça um programa que determine e mostre os cincos primeiros
múltiplos de 3, considerando números maiores que 0
"""

from collections.abc import Iterator
from locale import atoi, format_string


def get_multiples_of_three(n: int) -> Iterator[int]:
    """
    Take in 'n' to determinate the number of multiples to be returned
    :param n: number of desired multiples
    :return: Iterator with int values
    """
    for number in range(n + 1):
        if number != 0:
            yield number * 3


def main() -> None:
    print(
        '=' * 20
        + '\n'
        + 'MULTIPLOS DE 3'.center(20, '-')
        + '\n'
        + '=' * 20
        + '\n'
    )
    while True:
        try:
            multiples = atoi(input('Quantos multiplos você deseja?\n->  '))
            break
        except ValueError:
            print('Entrada inválida! Tente novamente...')
    numbers = tuple(get_multiples_of_three(multiples))
    formatted_numbers = ', '.join(format_string('%d', x) for x in numbers)
    print('\nValores:' f'\n{formatted_numbers}')


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:

print(
    '=' * 20 + '\n' +
    '5 MULTIPLOS DE 3'.center(20, '-') + '\n' +
    '=' * 20 + '\n'
)

for i in range(6):
    if i != 0 and i != 5:
        print(i * 3, end=', ')
    elif i != 0 and i == 5:
        print(i * 3)
"""
