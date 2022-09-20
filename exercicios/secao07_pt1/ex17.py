"""
17) Leia um vetor de 10 posições e atribua valor 0
para todos os elemntos que possírem valores negativos.
"""
from collections import deque
from collections.abc import Iterator
from locale import LC_ALL, atof, format_string, setlocale


def get_positive_value(n: int) -> Iterator[float]:
    for i in range(n):
        while True:
            try:
                value = atof(input(f'Enter {i + 1}º value:\n-> '))
                if value < 0:
                    value = 0
                yield value
                break
            except ValueError:
                print('Invalid value! Try again...\n')


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = deque(get_positive_value(10))
    formatted_numbers = ', '.join(format_string('%.1f', x) for x in numbers)
    print(
        '\nNumbers: \033[37mNegative numbers changed to 0\033[m'
        f'\n-> {formatted_numbers}.'
    )


if __name__ == '__main__':
    main()
