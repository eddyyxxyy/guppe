"""
48) Faça um programa que some os termos de valor par
da sequência de Fibonacci, cujos valores não ultrapassem quatro
milhões.
"""
from collections.abc import Iterator
from locale import atoi


def fibonacci_sequence(stop: int = 4_000_000) -> Iterator[int]:
    a, b = 0, 1
    for i in range(stop):
        if a > stop:
            break
        yield a
        a, b = b, a + b


def get_positive_int(msg: str = 'Enter a integer:\n-> ') -> int:
    while True:
        try:
            number: int = atoi(input(msg).strip())
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def main() -> None:
    numbers = tuple(fibonacci_sequence())
    print(numbers)
    print(sum([number for number in numbers if number % 2 == 0]))


if __name__ == '__main__':
    main()
