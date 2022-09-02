"""
33) Dados n e dois números inteiros positivos, i e j, diferentes de 0,
imprimir em ordem crescente os n primeiros naturais que são múltiplos
de i ou de j e ou de ambos. Exemplo: Para n = 6, i = 2 e j = 3 a saída
deverá ser: 0,2,3,4,6,8.
"""
from collections.abc import Iterator
from locale import atoi


def get_positive_integer(msg: str = 'Enter an integer:\n-> ') -> int:
    while True:
        try:
            number = atoi(input(msg).strip())
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def multiples_of_i_or_j() -> tuple[Iterator[int], tuple[int, int, int]]:
    n = get_positive_integer('Enter an integer for n:\n-> ')
    i = get_positive_integer('Enter an integer for i:\n-> ')
    j = get_positive_integer('Enter an integer for j:\n-> ')
    find_multiples = list()
    for number in range(n):
        if not (i * number in find_multiples):
            find_multiples.append(i * number)
        if not (j * number in find_multiples):
            find_multiples.append(j * number)
    find_multiples.sort()
    for number in range(n):
        yield find_multiples[number]
    yield n, i, j


def main():
    multiples = tuple(multiples_of_i_or_j())
    print(
        f'\nFirst {multiples[-1][0]} multiples of {multiples[-1][1]} and/or {multiples[-1][2]}:'
        f'\n-> {multiples[:-1]} | \033[37mIncluding zero\033[m'
    )


if __name__ == '__main__':
    main()
