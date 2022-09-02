"""
26) Faça um algoritmo que encontre o primeiro múltiplo de 11, 13
ou 17 após um número dado.
"""
from collections.abc import Iterator
from locale import atoi, setlocale, LC_ALL


def get_number(msg: str = 'Enter a number:\n-> ') -> int:
    while True:
        try:
            number: int = atoi(input(msg).strip())
            return number
        except ValueError:
            print('Invalid number! Try again...')


def show_multiple_of_11_13_17() -> tuple[float, int, int]:
    number: int = get_number()
    old_number: int = number
    while True:
        number += 1
        if number % 11 == 0:
            return number, 11, old_number
        elif number % 13 == 0:
            return number, 13, old_number
        elif number % 17 == 0:
            return number, 13, old_number


def main():
    setlocale(LC_ALL, 'pt-BR')
    first_mult = show_multiple_of_11_13_17()
    print(
        f'\nThe first number after {first_mult[2]} that can be divided by 11, 13 or 17:'
        f'\n-> {first_mult[0]} (divisible by {first_mult[1]})'
    )


if __name__ == '__main__':
    main()
