"""
59) Faça uma função que recebe, por parâmetro, 2 vetores de 10 elementos
inteiros e que calcule e retorne, também por parâmetro, o vetor união
dos dois primeiros.
"""
from random import sample

import numpy


def union_matrix(a, b):
    return numpy.concatenate((a, b))


def main() -> None:
    array_a = numpy.array(
        [
            sample(range(1, 11), 4),
            sample(range(1, 11), 4),
            sample(range(1, 11), 4),
            sample(range(1, 11), 4),
        ]
    )
    array_b = numpy.array(
        [
            sample(range(1, 11), 4),
            sample(range(1, 11), 4),
            sample(range(1, 11), 4),
            sample(range(1, 11), 4),
        ]
    )
    print(f'Array "A":\n {array_a}')
    print(f'\nArray "B":\n {array_a}')
    array_c = union_matrix(array_a, array_b)
    print(f'\nArray "C":\n {array_c}')


if __name__ == '__main__':
    main()
