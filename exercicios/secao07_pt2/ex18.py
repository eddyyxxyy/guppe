"""
18) Faça um programa que permita ao usuário entrar com uma matriz de
3 x 3 números inteiros. Em seguida, gere um array unidemensional
pela soma dos números de cada coluna da matriz e mostrar na tela
esse array. Por exemplo, a matriz:
    5   -8    10
    1    2   15
    25  10   7
Vai gerar um vetor, onde cada posição é a soma das colunas da matriz. A primeira
posição será 5 + 1 + 25, e assim por diante:
   31  4  32
"""
from locale import setlocale, LC_ALL, atoi


def get_int_array(rows: int, columns: int) -> list[list]:
    array = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    value = atoi(
                        input(f'Enter no. for [{i}, {j}]:\n-> ')
                    )
                    break
                except ValueError:
                    print('\033[31mINVALID NUMBER! Try again...\033[m\n')
            row.append(value)
        array.append(row)
    return array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array = get_int_array(3, 3)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    one_dimensional_array = []
    print('\nArray:')
    for row in array:
        print(row)
        sum1 += row[0]
        sum2 += row[1]
        sum3 += row[2]
    one_dimensional_array.append([sum1, sum2, sum3])
    print(
        '\nOne dimensional array:'
        f'\n-> {one_dimensional_array}'
    )


if __name__ == '__main__':
    main()
