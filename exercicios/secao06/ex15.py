"""
15) Faça um programa que leia um número inteiro positivo impar N e imprima
todos os números impares de 1 até N em ordem crescente.
"""
from collections.abc import Iterator
from locale import atoi


def get_positive_integer(msg: str = 'Enter a integer value: ') -> int:
    while True:
        try:
            number: int = atoi(input(msg + '\n-> ').strip())
            if number <= 0:
                continue
            return number
        except ValueError:
            print('Invalid value!\n')


def odd_til_n(invert: bool = False) -> Iterator[int]:
    number: int = get_positive_integer()
    if invert:
        for num in range(1, number + 1):
            if num % 2 != 0:
                yield num
    else:
        for num in range(number, 0, -1):
            if num % 2 != 0:
                yield num


def main():
    print('All odd numbers till "n"')
    while True:
        try:
            invert = atoi(
                input('\n(0)Descending or (1)Ascending order?\n-> ').strip()
            )
            if invert != 1 and invert != 0:
                print('Only type 0 or 1...\n')
                continue
            break
        except ValueError:
            print('Must be an integer...\n')
    odd_numbers = tuple(odd_til_n(bool(invert)))
    print('Odd numbers in ', end='')
    if invert == 0:
        print('descending order:')
    else:
        print('ascending order:')
    for index, value in enumerate(odd_numbers):
        if index == len(odd_numbers) - 1:
            print(f'{value}.')
        else:
            print(f'{value}, ', end='')


if __name__ == '__main__':
    main()
