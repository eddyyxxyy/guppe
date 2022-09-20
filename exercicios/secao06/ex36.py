"""
36) Faça um programa que calcule a diferença entre a soma dos quadrados
dos primeiros 100 números naturais e o quadrado da soma. Ex: A soma dos
quadrados dos dez primeiros números naturais é,
    1² + 2² + ... + 10² = 385
O quadrado da soma dos dez primeiros números naturais é,
    (1 + 2 + ... + 10)² = 552 = 3025
A diferença entre a soma dos quadrados dos dez primeiros números naturais
e o quadrado da soma é 3025-385 = 2640.
"""


def square_of_sums() -> int:
    sum_of: int = 0
    for number in range(1, 11):
        sum_of += number
    return sum_of**2


def sum_of_squares() -> int:
    sum_of: int = 0
    for number in range(1, 11):
        sum_of += number**2
    return sum_of


def main():
    sum_of = sum_of_squares()
    square_of = square_of_sums()
    print(
        'The diference between "a" and "b":'
        f'\na) Sum of squares, from 1 to 10: {sum_of};'
        f'\nb) Square of the sum, from 1 to 10: {square_of};'
        f'\nIs: {square_of - sum_of}'
    )


if __name__ == '__main__':
    main()
