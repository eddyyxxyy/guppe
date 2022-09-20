"""
11) Faça um programa que preencha um vetor com 10 números reais,
calcule e mostre a quantidade de números negativos e a soma dos números
positivos desse vetor.
"""
from collections.abc import Iterator
from locale import LC_ALL, atof, format_string, setlocale


def get_floats(n: int) -> Iterator[float]:
    for i in range(n):
        while True:
            try:
                number = atof(input(f'Enter the {i + 1}º number:\n-> '))
                yield number
                break
            except ValueError:
                print('Invalid number! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = tuple(get_floats(10))
    negative_nums = tuple(number for number in numbers if number < 0)
    formatted_numbers = ', '.join(format_string('%.1f', x) for x in numbers)
    formatted_negatives = ', '.join(
        format_string('%.1f', x) for x in negative_nums
    )
    print(
        '-' * 30 + '\nNumbers:'
        f'\n-> {formatted_numbers}.'
        '\nSum of Numbers:'
        f'\n-> {sum(number for number in numbers if number >= 0):n}.'
        '\nNegative numbers:'
        f'\n-> {formatted_negatives} -> {len(negative_nums)} negative numbers.'
    )


if __name__ == '__main__':
    main()
