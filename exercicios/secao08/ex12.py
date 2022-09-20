"""
12) Escreva uma função que receba um número inteiro maior que zero
e retorne a soma de todos os seus algarismos. Por exemplo,
ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido
não for maior do que zero, o programa terminará com a mensagem "Número inválido"
"""
from locale import LC_ALL, atoi, format_string, setlocale


def get_positive_int() -> int:
    while True:
        try:
            value = atoi(input('Enter positive integer:\n-> '))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print('Invalid! Try again...')


def sum_of_algaris() -> list[int]:
    value = get_positive_int()
    return list(map(int, str(value)))


def main() -> None:
    setlocale(LC_ALL, '')
    value = sum_of_algaris()
    formatted_value = ', '.join(format_string('%d', x) for x in value)
    print(
        '\n\nNumbers:'
        f'\n-> {formatted_value}.'
        '\nSum of Numbers:'
        f'\n-> {sum(value):n}'
    )


if __name__ == '__main__':
    main()
