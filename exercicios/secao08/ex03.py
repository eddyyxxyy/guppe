"""
3) Faça uma função para verificar se um número é positivo ou negativo.
Sendo que o valor de retorno será 1 se positivo, -1 se negativo
e 0 se for igual a 0
"""
from locale import LC_ALL, setlocale


def check_number(n: int) -> int:
    if n == 0:
        return 0
    elif n > 0:
        return 1
    else:
        return -1


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    print(check_number(0))
    print(check_number(25))
    print(check_number(-25))


if __name__ == '__main__':
    main()
