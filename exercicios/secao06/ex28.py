"""
28) Faça um porgrama que leia um valor N inteiro e positivo,
calcule e mostre o valor E, conforme a fórmula a seguir
    E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
"""
from locale import atoi
from math import factorial


def get_integer(msg: str = 'Enter an integer:\n-> ') -> int:
    while True:
        try:
            number = atoi(input(msg).strip())
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def e_value() -> float:
    number = get_integer()
    value: float = 0
    for num in range(1, number + 1):
        value += float(num) / factorial(num)
    return value


def main() -> None:
    number = e_value()
    print(
        '\nSum of the series:'
        f'\n-> {number}'
    )


if __name__ == '__main__':
    main()
