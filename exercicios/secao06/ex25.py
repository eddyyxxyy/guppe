"""
25) Faça um programa que some todos os números naturais abaixo de 1000
que são múltiplos de 3 ou 5.
"""
from collections.abc import Iterator


def n_before_1000() -> Iterator[int]:
    for number in range(1, 1000):
        if number % 3 == 0 or number % 5 == 0:
            yield number


def main() -> None:
    print(
        'Numbers up to 1000 that are divisible by 3 or 5:'
        f'\n-> {sum(n_before_1000())}'
    )


if __name__ == '__main__':
    main()
