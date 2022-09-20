"""
43) Faça um programa que leia um número inderterminado de idades de
indivíduos (pare quando for informada a idade 0), e calcule a idade
média desse grupo.
"""
from collections.abc import Iterator
from locale import atoi


def get_age(
    msg: str = 'Enter an age: \033[37m0 to exit\033[m\n-> ',
) -> Iterator[int | None]:
    while True:
        try:
            age: int = atoi(input(msg).strip())
            if age <= 0:
                return None
            yield age
        except ValueError:
            print('Invalid age! Try again...\n')


def average_age() -> float:
    ages = tuple(get_age())
    return sum(ages) / len(ages)


def main():
    ages = average_age()
    print(
        '\nAverage age between the informed values:' f'\n-> {ages:.2f} years.'
    )


if __name__ == '__main__':
    main()
