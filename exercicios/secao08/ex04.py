"""
4) Faça uma função para verificar se um número é um quadrado perfeito.
Um quadrado perfeito é um número inteiro não negativo que pode ser
expresso como o quadrado de outro número inteiro. Ex: 1, 4, 9...
"""
from locale import setlocale, LC_ALL, atoi

from numpy import sqrt


def check_perf_square(x: int) -> bool:
    if x >= 0:
        sr = sqrt(x)
        return (sr * sr) == x
    return False


def get_int():
    while True:
        try:
            number = atoi(
                input('Enter an integer:\n-> ')
            )
            return number
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def main() -> None:
    setlocale(LC_ALL, '')
    value = get_int()
    if check_perf_square(value):
        print(f'\n{value:n} is a perfect square.')
    else:
        print(f'\n{value:n} is a perfect square.')


if __name__ == '__main__':
    main()
