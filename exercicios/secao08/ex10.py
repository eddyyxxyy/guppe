"""
10) Faça uma função que receba dois números e retorne qual deles é o maior.
"""
from locale import LC_ALL, setlocale

from exercicios.secao08.ex09 import get_float


def which_is_larger(a, b):
    return max(a, b), 'b' if b > a else 'a'


def main() -> None:
    setlocale(LC_ALL, '')
    a = get_float('"a"')
    b = get_float('"b"')
    larger = which_is_larger(a, b)
    print(
        '\na:'
        f'\n-> {a:n}'
        '\nb:'
        f'\n-> {b:n}'
        '\nGreater value:'
        f'\n-> {larger[1]} -> {larger[0]:n}'
    )


if __name__ == '__main__':
    main()
