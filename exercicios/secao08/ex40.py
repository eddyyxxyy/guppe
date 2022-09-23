"""
40) Faça uma função que receba um vetor de inteiros e retorne
quantos valores pares ele possui.
"""
from collections.abc import Iterable


def is_even(num: int) -> True | False:
    return num % 2 == 0


def count_even_in_array(array: Iterable) -> int:
    count = 0
    for element in array:
        if is_even(element):
            count += 1
    return count


def main() -> None:
    tuple = (
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
    )
    result = count_even_in_array(tuple)
    print(
        'Array:'
        f'\n{tuple}'
        '\nCount of even number in array:'
        f'\n-> {result}'
    )


if __name__ == '__main__':
    main()
