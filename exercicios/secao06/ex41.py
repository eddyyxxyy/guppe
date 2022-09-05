"""
41) Faça um programa que calcula a associação em paralelo de dois resistores
R1 e R2 fornecidos pelo usuário via teclado. O programa fica pedindo estes
valores e calculando até que o usuário entre com um valor para resistência igual a zero.
    R = (R1 * R2) / (R1 + R2)
"""
from collections.abc import Iterator
from locale import atof


def get_number(msg: str = 'Enter a number:\n-> ') -> float:
    while True:
        try:
            number: float = atof(input(msg).strip())
            return number
        except ValueError:
            print('Invalid! Try again...\n')


def resistors() -> Iterator[float]:
    while True:
        r1 = get_number('Enter a number for r1:\n-> ')
        if r1 <= 0:
            break
        r2 = get_number('Enter a number for r2:\n-> ')
        if r2 <= 0:
            break
        yield (r1 * r2) / (r1 + r2)


def main():
    resistors_results = tuple(resistors())
    print(
        '\nParallel association of every pair of resistors:'
        f'\n-> {resistors_results}'
    )


if __name__ == '__main__':
    main()
