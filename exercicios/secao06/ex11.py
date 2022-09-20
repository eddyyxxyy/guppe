"""
11) faça um programa que leia um número inteiro positivo N
e imprima todos os números naturais de 0 até N em ordem crescente.
"""

from collections.abc import Iterator
from locale import atoi, format_string


def n_natural_numbers(times: int, inverse: bool = True) -> Iterator[int]:
    if not inverse:
        for number in range(0, times + 1):
            yield number
    else:
        for number in range(times, -1, -1):
            yield number


def main():
    while True:
        try:
            times: int = atoi(
                input('How many even numbers you want to sum?\n-> ')
            )
            break
        except ValueError:
            print('Invalid input! Try again...')
    while True:
        try:
            inverse: int = atoi(input('(0)Ascending or (1)Descending?\n-> '))
            if inverse != 0 and inverse != 1:
                continue
            break
        except ValueError:
            print('Invalid input! Try again...')
    numbers = tuple(n_natural_numbers(times, bool(inverse)))
    formatted_numbers = ', '.join(format_string('%d', x) for x in numbers)
    print('\nNumbers:' f'\n-> {formatted_numbers}')


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:

print(
    '=' * 20 + '\n' +
    'N NÚMEROS NATURAIS'.center(20, '-') + '\n' +
    '=' * 20 + '\n'
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
            while i < number + 1:
                if i == number:
                    print('\033[32;1m↓')
                print(i)
                i += 1
            print('\033[m')
            break
"""
