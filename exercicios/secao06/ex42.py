"""
42) Faça um programa que leia um conjunto não determinado de valores,
um de cada vez, e escreva para cada um dos valores lidos, o quadrado,
o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.
"""
from collections.abc import Iterator
from locale import atof
from math import sqrt


def get_number(msg: str = 'Enter a number:\n-> ') -> float:
    while True:
        try:
            number: float = atof(input(msg).strip())
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def set_of_numbers() -> Iterator[dict] | None:
    while True:
        value = get_number(
            'Enter a number: \033[37m0 or less to exit\033[m\n-> '
        )
        if value <= 0:
            return None
        yield dict(
            number=value,
            square=value**2,
            cubic=value**3,
            sqrroot=sqrt(value),
        )


def main():
    values = tuple(set_of_numbers())
    for dicts in values:
        print(f'\n{dicts}')


if __name__ == '__main__':
    main()
