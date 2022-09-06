"""
52) Escreva um programa que receba como entrada o valor do saque
realizado pelo cliente de um banco e retorne quantas notas de cada valor
serão necessárias para atender ao saque com a menor quantidade de notas possível.
Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""
from collections.abc import Iterator
from locale import atof


def get_value(msg: str = 'Enter a value:\n-> \033[37m$\033[m') -> float:
    while True:
        try:
            value: float = atof(input(msg))
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            print('Invalid amount of money! Try again...\n')


def bank() -> Iterator:
    value = get_value()
    banknotes = (100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00)
    yield f'R${value:.2f}:'
    for x in banknotes:
        yield f'{int(value / x)} banknotes of R${x:.2f}'
        value %= x


def main() -> None:
    value = tuple(bank())
    for value in value:
        if value[0] != '0':
            print(value)


if __name__ == '__main__':
    main()
