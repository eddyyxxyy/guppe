"""
17) Faça um programa que leia um número inteiro positivo
n e calcule a soma dos n primeiros números naturais.
"""
from collections.abc import Iterator
from locale import atoi


def input_positive_integer() -> int:
    while True:
        try:
            number: int = atoi(input('Enter a positive integer:\n-> ').strip())
            if number <= 0:
                print('Number must be a positive integer...\n')
                continue
            return number
        except ValueError:
            print('Invalid value!\n')


def sum_first_natural_numbers() -> Iterator[int]:
    number: int = input_positive_integer()
    for num in range(1, number + 1):
        yield num


def main():
    numbers = tuple(sum_first_natural_numbers())
    print(
        '\nNumbers:'
        f'\n-> {numbers}'
        '\nSum of all numbers:'
        f'\n-> {sum(numbers)}'
    )


if __name__ == '__main__':
    main()
