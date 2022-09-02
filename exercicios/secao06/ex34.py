"""
34) Faça um programa que calcule o menor número divisível por cada
um dos números de 1 a 20. Ex: 2520 é o menor número que pode ser
dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""
from collections.abc import Iterator
from math import lcm


def find_mmc(start: int = 2, end: int = 21) -> Iterator[int, tuple]:
    yield lcm(*range(start, end))
    yield start, end


def main():
    operation = tuple(find_mmc(1, 20))
    number = operation[0]
    print(
        f'The mmc of {operation[1][0]} to {operation[1][1]} is:'
        f'\n-> {number}'
    )


if __name__ == '__main__':
    main()
