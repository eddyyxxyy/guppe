"""
14) Dado um arquivo contendo um conjunto de nome e data nascimento (DD MM AAAA,
isto é, 3 inteiros em sequência), faça um programa que leia o nome do arquivo
e a data de hoje e construa outro arquivo contendo o nome e a idade de cada
pessoa do primeiro arquivo.
"""
from datetime import date


def main() -> None:
    with open('arquivos/ex14_arq.txt') as f, \
            open('arquivos/ex14_arq1.txt', 'w') as f1:
        for row in f.readlines():
            birth = int(row[20:].split('/')[0])
            today = int(date.today().year)
            age = today - birth
            f1.write(row[:20] + str(age) + " years\n")


if __name__ == '__main__':
    main()
