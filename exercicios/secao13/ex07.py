"""
7) Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo
texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por '*'
"""


def replace_vowels(path: str):
    with open(path, 'r', encoding='UTF-8') as f:
        result = f.read()
        result = (
            result.replace('a', '*')
            .replace('e', '*')
            .replace('i', '*')
            .replace('o', '*')
            .replace('u', '*')
        )
    with open('arquivos/ex07_arq2.txt', 'w+', encoding='UTF-8') as f:
        f.write(result)


def main() -> None:
    replace_vowels('arquivos/ex07_arq.txt')
    with open('arquivos/ex07_arq2.txt', 'r', encoding='UTF-8') as f:
        print(f.read())


if __name__ == '__main__':
    main()
