"""
33) Faça uma função que receba um número N e retorne a soma dos algarismos de N!.
Ex: se N = 4, N! = 24. logo, a soma de seus algarismos é 2 + 4 = 6.
"""
from math import factorial


def get_positive_int(prompt: str) -> int:
    while True:
        try:
            integer = int(input(prompt))
            if integer <= 0:
                raise ValueError
            return integer
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def sum_algarisms_of_fact(n: int) -> tuple:
    n_algarisms = tuple(int(algarism) for algarism in str(factorial(n)))
    return n_algarisms, sum(n_algarisms)


def main() -> None:
    n = get_positive_int('Enter positive integer: ')
    result = sum_algarisms_of_fact(n)
    print(
        f'Sum of algarisms of {n}!:'
        f'\n-> {result[1]} -> {n}! algarisms = {result[0]}'
    )


if __name__ == '__main__':
    main()
