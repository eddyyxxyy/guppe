"""
18) Faça um programa que leia um arquivo contendo o nome e o preço de diversos
produtos (separados por linha), e calcule o total da compra.
"""


def main() -> None:
    with open('arquivos/ex18_products.txt') as f:
        result = 0
        for row in f.read().split(','):
            result += float(row.split()[1])
        print(result)


if __name__ == '__main__':
    main()
