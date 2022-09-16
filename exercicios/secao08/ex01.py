"""
1) Crie uma função que recebe como parâmetro um número inteiro e devolve
o seu dobro.
"""
from locale import setlocale, LC_ALL


def double_int(n: int) -> int:
    return n * 2


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a = double_int(5)
    print(a)


if __name__ == '__main__':
    main()
