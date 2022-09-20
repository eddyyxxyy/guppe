"""
13) Fazer um programa ler 5 valores e, em seguida, mostrar a posição onde
se encotram o maior e o menor valor.
"""
from locale import LC_ALL, format_string, setlocale

from ex12 import get_values


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = tuple(get_values(5))
    formatted_numbers = ', '.join(
        format_string('%.1f', x, grouping=True) for x in numbers
    )
    print(
        '-' * 30 + '\nNumbers:'
        f'\n-> {formatted_numbers}.'
        '\nMax:'
        f'\n-> {max(numbers):n} -> in position {numbers.index(max(numbers))}'
        '\nMin:'
        f'\n-> {min(numbers):n} -> in position {numbers.index(min(numbers))}'
    )


if __name__ == '__main__':
    main()
