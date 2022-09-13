"""
3) Faça um programa que preenche uma matriz 4 x 4 com o produto do valor da linha
e da coluna de cada elemento. Em seguida, imprima na tela a matriz.
"""


def main() -> None:
    array = []
    for row in range(4):
        array1 = []
        for column in range(4):
            array1.append(row * column)
        array.append(array1)
    for row in range(4):
        for column in range(4):
            print(array[row][column], end='  ')
        print()


if __name__ == '__main__':
    main()
