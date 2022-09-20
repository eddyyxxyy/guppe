"""
2) Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0
os demais elementos. Escreva ao final matriz obtida
"""
from locale import LC_ALL, setlocale


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array = []
    for i in range(5):
        array1 = []
        for j in range(5):
            if i == j:
                array1.append(1)
            else:
                array1.append(0)
        array.append(array1)
    for row in range(4):
        for column in range(4):
            print(array[row][column], end='  ')
        print()


if __name__ == '__main__':
    main()
