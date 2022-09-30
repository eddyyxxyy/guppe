"""
5) Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre
na tela quantas vezes aquele caractere ocorre dentro do arquivo.
"""


def count_char(path: str, char: str):
    with open(path, mode='r', encoding='UTF-8') as arq:
        return arq.read().count(char)


def main() -> None:
    result = count_char('arquivos/ex05_arq.txt', 'a')
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
