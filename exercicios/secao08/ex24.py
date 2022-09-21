"""
24) Escreva uma função que gera um triângulo de altura e lados n e base
2*n-1. Por Exemplo, a saída para n = 6 seria:
              *
             ***
            *****
           *******
          *********
         ***********
"""
from exercicios.secao08.ex22 import get_int


def asterisk_tree(numero: int) -> str:
    my_list = []
    result_string = ''
    for i in range(numero + 1):
        for j in range(numero):
            if i == numero - j:
                my_list.append((' ' * j) + ('*' * (2 * i - 1)))
    for element in my_list:
        result_string += element + '\n'
    return result_string


def main() -> None:
    size = get_int('Enter the size of the asterisk triangle:\n-> ')
    at = asterisk_tree(size)
    print(at)


if __name__ == '__main__':
    main()
