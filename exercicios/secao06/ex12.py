"""
12) Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem decrescente
"""

from collections.abc import Iterator
from locale import atoi, format_string


def n_natural_numbers(times: int, inverse: bool = False) -> Iterator[int]:
    if inverse:
        for number in range(0, times + 1):
            yield number
    else:
        for number in range(times, -1, -1):
            yield number


def main():
    print('All the numbers till "n"')
    while True:
        try:
            times: int = atoi(input('Enter a number:\n-> '))
            if times <= 0:
                print('Invalid input! Try again...')
                continue
            break
        except ValueError:
            print('Invalid input! Try again...')
    while True:
        try:
            inverse: int = atoi(input('(1)Ascending or (0)Descending?\n-> '))
            if inverse != 0 and inverse != 1:
                print('Invalid input! Try again...')
                continue
            break
        except ValueError:
            print('Invalid input! Try again...')
    numbers = tuple(n_natural_numbers(times, bool(inverse)))
    formatted_numbers = ", ".join(
        format_string("%d", x) for x in numbers
    )
    print(
        '\nNumbers:'
        f'\n-> {formatted_numbers}'
    )


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:

print(
    '=' * 35 + '\n' +
    'N NÚMEROS NATURAIS (INVERSAMENTE)'.center(35, '-') + '\n' +
    '=' * 35 + '\n'
)

number: int = 0
i: int = 0

while True:
    try:
        number = int(input('Informe um número inteiro positivo: ').strip())
    except ValueError:
        print('Valor inválido! Tente novamente...\n')
    else:
        if number <= 0:
            print('Valor inválido! Tente novamente...\n')
        else:
            print()
            for i in range(number, -1, -1):
                if i == number:
                    lenght = len(str(i))
                    print(f'\033[32;1m{i}')
                    print('\033[32;1m' + '↑'.center(lenght))
                else:
                    print('\033[m' + f'{i}')
                    i += 1
            break
"""