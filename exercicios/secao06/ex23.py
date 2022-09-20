"""
23) Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""
from locale import atoi, format_string
from typing import Iterator


def get_number(msg: str = 'Enter a number:\n-> ') -> int:
    while True:
        try:
            number = atoi(input(msg).strip())
            return number
        except ValueError:
            print('invalid number! Try again...')


def divisors() -> Iterator[int]:
    number = get_number('Enter a positive integer:\n-> ')
    if number <= 0:
        yield 0
    for num in range(1, number + 1):
        if number % num == 0:
            yield num


def main() -> None:
    number_dividers = tuple(divisors())
    formatted_dividers = ', '.join(
        format_string('%d', x) for x in number_dividers
    )
    print(
        f'\nDividers for {number_dividers[-1]}:' f'\n-> {formatted_dividers}.',
        end='\n',
    )
    if len(number_dividers) == 2 or len(number_dividers) == 1:
        print(f'{number_dividers[-1]} is a prime number!')


if __name__ == '__main__':
    main()
