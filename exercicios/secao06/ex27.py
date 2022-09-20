"""
27) Em Matemática, o número harmônico designado por H(n) define-se
como sendo a soma da série harmônica:
    H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""
from collections.abc import Iterator
from locale import atoi


def get_integer(msg: str = 'Enter a positive integer:\n-> ') -> int:
    while True:
        try:
            number: int = atoi(input(msg).strip())
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...')


def harmonic_number() -> Iterator[float]:
    number: int = get_integer()
    for num in range(1, number + 1):
        if num == 1:
            yield 1
        else:
            yield 1 / num


def main() -> None:
    harmo_num = tuple(harmonic_number())
    print('\nsum of the harmonic series:' f'\n-> {sum(harmo_num)}')


if __name__ == '__main__':
    main()
