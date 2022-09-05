"""
40) Elabore um programa que faça leitura de vários números inteiros, até que se
digite um número negativo. O programa tem que retornar o maior e o menor
número lido.
"""
from collections.abc import Iterator
from locale import atof


def get_positive_numbers(msg: str = 'Enter a number:\n-> ') -> Iterator[float]:
    while True:
        try:
            number: float = atof(input(msg).strip())
            if number < 0:
                break
            yield number
        except ValueError:
            print('Invalid! Try again...\n')


def main() -> None:
    numbers: tuple = tuple(get_positive_numbers())
    print(
        '\nNumbers:'
        f'\n-> {numbers}'
        '\nMax:'
        f'\n-> {max(numbers)}'
        '\nMin:'
        f'\n-> {min(numbers)}'
    )


if __name__ == '__main__':
    main()
