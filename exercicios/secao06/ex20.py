"""
20) Ler uma sequência de números inteiros e determinar se eles são pares
ou não. Deverá ser informado o número de dados lidos e números de valores
pares. O processo termina quando for digitado o número 1000.
"""
from collections.abc import Iterator
from locale import atoi, format_string


def input_integer(msg: str) -> Iterator[int] or int:
    number: int = 0
    while number != 1000:
        try:
            number = atoi(input(msg).strip())
            if number == 1000:
                break
            yield number
        except ValueError:
            print('Number must be integer...\n')


def main():
    print('\033[37mEven Numbers\033[m\n')
    numbers = tuple(
        input_integer('Enter an integer: \033[37m1000 to exit\033[m\n-> ')
    )
    formatted_numbers = ', '.join(format_string('%d', x) for x in numbers)
    print(
        '\nNumbers:'
        f'\n-> {formatted_numbers}.'
        '\nHow many numbers we have?'
        f'\n-> {len(numbers)}'
        '\nAnd even numbers?'
        f'\n-> {len([num for num in numbers if num % 2 == 0])}'
    )


if __name__ == '__main__':
    main()
