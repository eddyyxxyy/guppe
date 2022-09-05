"""
37) Escreve um programa que verifique quais os números entre 1000 e 9999
(inclusive) possuem a propriedade seguinte: a soma dos dois dígitos de
mais baixa ordem com os dois dígitos de mais alta ordem elevada ao quadrado
é igual ao próprio número. Por exemplo, para o inteiro 3025, temos que:
30 + 25 = 55
55² = 3025
"""
from collections.abc import Iterator


def between_thousands() -> Iterator[int]:
    for number in range(1000, 10000):
        if (int(str(number)[:2]) + int(str(number)[2:])) ** 2 == number:
            yield number


def main():
    numbers = tuple(between_thousands())
    print(
        'Numbers that, if you sum their first 2 digits with the other 2 and then multiply the result, end up being the '
        'same number:'
        f'\n-> {numbers}'
    )


if __name__ == '__main__':
    main()
