"""
21) Faça um programa que receba dois números. Calcule e mostre:
    - A soma dos números pares desse intervalo de números, incluindo
os números digitados;
    - A multiuplicação dos números ímpares desse intervalo, incluindo
os digitados;
"""
from collections.abc import Iterator
from locale import atoi, format_string
from math import prod


# from math import prod


def input_integer(prompt: str = 'Enter a number:\n-> ') -> int:
    """
    Take an integer and return it
    :param prompt: message shown to user
    :return: int
    """
    while True:
        try:
            n = atoi(input(prompt).strip())
            return n
        except ValueError:
            print('Number must be an integer!\n')


def numbers_between() -> Iterator[int]:
    """
    Take 2 integers and return the numbers
    between first number and second number
    as a generator
    :return: generator object
    """
    start_n = input_integer()
    end_n = input_integer()
    if start_n >= end_n:
        for number in range(end_n, start_n + 1):
            yield number
    if end_n > start_n:
        for number in range(start_n, end_n + 1):
            yield number


def main() -> None:
    numbers = tuple(numbers_between())
    formatted_numbers = ", ".join(
        format_string("%d", x) for x in numbers
    )
    print(
        '\nNumbers:'
        f'\n-> {formatted_numbers}'
        '\nSum of even numbers:'
        f'\n-> {sum([number for number in numbers if number % 2 == 0])}'
        '\nMultiplication of odd numbers:'
        f'\n-> {prod([number for number in numbers if number % 2 != 0])}'
    )
    # using functools.reduce to show the same results:
    # f'\n-> {reduce((lambda x, y: x * y), [number for number in numbers if number % 2 != 0])}'


if __name__ == '__main__':
    main()
