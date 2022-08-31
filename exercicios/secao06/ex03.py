"""
3) Faça um algoritmo utilizando o comando while que mostra uma mensagem
regressiva na tela, inciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!"
após a contagem
"""
from locale import atoi, format_string
from collections.abc import Iterator


def n_to_zero(n: int = 10) -> Iterator[int]:
    number = n
    while number >= 0:
        yield number
        number -= 1


def main():
    print(
        '=' * 8 + '\n' +
        'N TO 0'.center(8, '-') + '\n' +
        '=' * 8 + '\n'
    )
    while True:
        try:
            number = atoi(input('Start: '))
            break
        except ValueError:
            print('Invalid input! Try again...')
    numbers = tuple(n_to_zero(number))
    formatted_numbers = ', '.join(
        format_string("%d", x) for x in numbers
    )
    print(formatted_numbers, end=' → END')


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:
print(
    '=' * 21 + '\n' +
    'DE 10 A 0 (WHILE)'.center(21, '-') + '\n' +
    '=' * 21 + '\n'
)

cont: int = 10
while cont != -1:
    print(cont, end=', ')
    cont -= 1
print('FIM!')
"""
