"""
2) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas linhas esse arquivo possui
"""


def count_lines(path: str) -> int:
    with open(path, 'r', encoding='UTF-8') as arq:
        res = arq.read()
        res = res.split('\n')
        return len(res)


def main() -> None:
    result = count_lines('arquivos/ex02_arq.txt')
    print(f'Number of lines the txt has: {result}')


if __name__ == '__main__':
    main()
