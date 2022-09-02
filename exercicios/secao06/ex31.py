"""
31) Faça um programa que calcule o valor de S
    S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50
"""


def calc_sequence() -> float:
    s = 0
    x = tuple(range(1, 100, 2))
    y = tuple(range(1, 51))
    for i in range(50):
        s += x[i] / y[i]
    return float(s)


def main() -> None:
    sequence_result = calc_sequence()
    print(
        'Sequence:'
        f'\n-> S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50'
        '\nResult:'
        f'\n-> S = {sequence_result}'
    )


if __name__ == '__main__':
    main()
