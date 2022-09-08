"""
14) Faça um programa que leia um vetor de 10 posições e verifique se existem
valores iguais e os escreva na tela.
"""
from locale import setlocale, LC_ALL, format_string

from ex12 import get_values


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = tuple(get_values(10))
    duplicated_numbers = set(
        (x for x in numbers if numbers.count(x) > 1)
    )
    formatted_numbers = ' - '.join(
        format_string('%.1f', x, grouping=True) for x in numbers
    )
    formatted_duplicate_numbers = ' - '.join(
        format_string('%.1f', x, grouping=True) for x in duplicated_numbers
    )
    print(
        '-' * 30 +
        '\nNumbers:'
        f'\n-> {formatted_numbers}.'
        '\nDuplicated numbers:'
        f'\n-> {formatted_duplicate_numbers}.'
    )


if __name__ == '__main__':
    main()
