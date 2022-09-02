"""
30) Faça programas para calcular as seguintes sequências:
    1 + 2 + 3 + 4 + 5 + ... + n
    1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
    1 + 3 + 5 + 7 + ... + (2n - 1)

# Não tenho certeza sobre a sequência 2.
"""
from locale import atoi


def get_integer(msg: str = 'Enter an integer:\n-> ') -> int:
    while True:
        try:
            number = atoi(input(msg).strip())
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...')


def sequences() -> tuple[int, int, int, int]:
    termos = get_integer()
    calculo1 = 0
    calculo2 = 0
    calculo3 = 0
    for i in range(1, termos + 1):
        calculo1 += i
        if i == termos:
            if i % 2 == 0:
                calculo2 += -i + (2 * termos - 1)
            elif i % 2 == 1:
                calculo2 += i + (2 * termos - 1)
                calculo3 += i
            calculo3 += (2 * termos - 1)
            break
        if i % 2 == 0:
            calculo2 -= i
        elif i % 2 == 1:
            calculo2 += i
            calculo3 += i
    return termos, calculo1, calculo2, calculo3


def main() -> None:
    seq = sequences()
    print(
        'Sequences:'
        f'\n1: 1 + 2 + 3 + 4 + 5 + ... + n -> {seq[1]}'
        f'\n2: 1 - 2 + 3 - 4 + 5 + ... + (2n - 1) -> {seq[2]}'
        f'\n3: 1 + 3 + 5 + 7 + ... + (2n - 1) -> {seq[3]}'
    )


if __name__ == '__main__':
    main()
