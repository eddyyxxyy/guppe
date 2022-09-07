"""
54) Faça um programa que receba um número inteiro maior do que 1,
e verifique se o número fornecido é primo ou não.
"""
from locale import atoi


def get_positive_num(msg: str) -> int:
    while True:
        try:
            number: int = atoi(input(msg))
            if number < 1:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def main() -> None:
    number = get_positive_num('Enter an positive integer:\n-> ')
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    if counter == 2:
        print(f'{number} is a prime number.')
    else:
        print(f'{number} is not a prime number.')


if __name__ == '__main__':
    main()
