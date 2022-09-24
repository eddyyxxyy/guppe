"""
43) Faça uma função que receba um vetor de inteiros e o preencha
com números aleatórios sem repetição.
"""
from random import randint


def random_num_array(*args) -> list:
    array = set(args)
    while len(array) < len(args):
        array.add(randint(1, 99))
    return list(array)


def main() -> None:
    print(random_num_array(1, 2, 3, 3, 3, 3, 5, 7, 8, 9, 11, 11))


if __name__ == '__main__':
    main()
