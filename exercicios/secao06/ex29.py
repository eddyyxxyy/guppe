"""
29) Escreva um programa para calcular o valor da série,
para 5 termos.
    S = 0 + 1/2! + 2/4! + 3/6! + ...
"""
from locale import atoi
from math import factorial


def get_integer(msg: str = 'Enter an integer:\n-> ') -> int:
    while True:
        try:
            number = atoi(input(msg).strip())
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def series_value(n: int = 5) -> float:
    value: float = 0
    for num in range(1, n + 1):
        value += num / factorial(num * 2)
    return value


def main():
    number = get_integer('Enter an integer for series S:\n-> ')
    serie = series_value(number)
    print(
        f'\nSum of the series ({number}):'
        f'\n-> {serie}'
    )


if __name__ == '__main__':
    main()
