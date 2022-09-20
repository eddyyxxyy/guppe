"""
15) Leia um vetor com 20 números inteiros. Escreva os elementos do vetor
eliminando elementos repetidos.
"""
from locale import LC_ALL, format_string, setlocale

from exercicios.secao07_pt1.ex07 import get_ints


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = tuple(get_ints(20))
    numbers_no_duplicates = set(numbers)
    formatted_numbers = ' - '.join(format_string('%d', x) for x in numbers)
    formatted_no_duplicates = ' - '.join(
        format_string('%d', x) for x in numbers_no_duplicates
    )
    print(
        '-' * 30 + '\nNumbers:'
        f'\n-> {formatted_numbers}'
        '\nNumbers without duplicates:'
        f'\n-> {formatted_no_duplicates}'
    )


if __name__ == '__main__':
    main()
