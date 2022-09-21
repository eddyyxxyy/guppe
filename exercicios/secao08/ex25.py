"""
25) Faça uma funçao que receba um inteiro N como parâmetro, calcule e retorne
o resultado da seguinte série:
    S = 2/4 + 5/5 + 10/6 + ... + (N² + 1)/(N + 3)
"""
from locale import LC_ALL, setlocale

from exercicios.secao08.ex22 import get_int


def series(number: int) -> float:
    result = 0
    for num in range(1, number + 1):
        result += (num**2 + 1) / (num + 3)
    return result


def main() -> None:
    setlocale(LC_ALL, '')
    number = get_int('Enter "n" for series:\n-> ')
    result = series(number)
    print(
        '\nS:'
        '\n-> S = 2/4 + 5/5 + 10/6 + ... + (N² + 1)/(N + 3)'
        '\nNumber:'
        f'\n-> {number:n}'
        '\nResult:'
        f'\n-> {result:n}'
    )


if __name__ == '__main__':
    main()
