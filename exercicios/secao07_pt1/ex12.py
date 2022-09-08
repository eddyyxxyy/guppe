"""
12) Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores
lidos juntamente com o maior, o menor e a média dos valores.
"""
from collections.abc import Iterator
from locale import setlocale, LC_ALL, atof, format_string


def get_values(n: int) -> Iterator[float]:
    """
    Input n floats and yields the value n times
    :param n: amount of iterations to yield float values
    :return: Iterator with floats
    """
    for i in range(n):
        while True:
            try:
                number = atof(
                    input(f'Enter {i + 1}º number:\n-> ')
                )
                yield number
                break
            except ValueError:
                print('Invalid number! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = tuple(get_values(5))
    formatted_numbers = ', '.join(
        format_string('%.1f', x, grouping=True) for x in numbers
    )
    print(
        '-' * 30 +
        '\nNumbers:'
        f'\n-> {formatted_numbers}'
        '\nAverage of Numbers:'
        f'\n-> {sum(numbers) / len(numbers):n}'
        '\nMax:'
        f'\n-> {max(numbers):n}'
        '\nMin:'
        f'\n-> {min(numbers):n}'
    )


if __name__ == '__main__':
    main()
