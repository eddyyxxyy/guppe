"""
16) Faça um programa que recebe um vetor de 10 números, converta
cada um desses números para binário e grave a sequência de 0s e 1s
em um arquivo texto. Cada número deve ser gravado em uma linha.
"""


def main() -> None:
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with open('arquivos/ex16_arq.txt', 'w') as f:
        for num in array:
            f.write(format(num, 'b') + '\n')


if __name__ == '__main__':
    main()
