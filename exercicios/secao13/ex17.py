"""
17) Faça um programa que leia um arquivo que contenha as dimensões de uma
matrix (linha e coluna), a quantidade de posições que serão anuladas, e as
posições a serem anuladas (linha e coluna). O programa lê esse arquivo e,
em seguida, produz um novo arquivo com a matriz com as dimensões dadas
no arquivo lido, e todas as posições especificadas no arquivo ZERADAS e o
restante recebendo o valor 1.
Ex: arquivo "matriz.txt"
3 3 2 /*3 e 3 dimensões da matriz e 2 posições que serão anuladas*/
1 0
1 2   /*Posições da matriz que serão anuladas.
arquivo "matriz_saida.txt"
saida:
1 1 1
0 1 0
1 1 1
"""


def main() -> None:
    with open('arquivos/ex17_matrix_output.txt') as f:
        line0 = f.readline().split()
        line1 = f.readline().split()
        line2 = f.readline().split()
        array = []
        for row in range(int(line0[0])):
            array.append([])
            for column in range(int(line0[1])):
                if row == int(line1[0]) and column == int(line1[1]) or \
                        row == int(line2[0]) and column == int(line2[1]):
                    array[row].append(0)
                else:
                    array[row].append(1)
        for row in array:
            print(row)


if __name__ == '__main__':
    main()
