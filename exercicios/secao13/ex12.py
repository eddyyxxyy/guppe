"""
12) Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas
e o número de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre
no arquivo (ignorando letras com acento). Obs.: palavras são separadas por um ou mais
caracteres espaços, tabulação ou nova linha.
"""
from string import ascii_lowercase


def main() -> None:
    with open('arquivos/ex12_arq.txt') as f:
        amount_chars = len(f.read())
        f.seek(0)
        amount_rows = len(f.readlines())
        f.seek(0)
        amount_each_letter = []
        for char in ascii_lowercase:
            f.seek(0)
            amount_each_letter.append({char: f.read().lower().count(char)})
    print(
        'Lenght of ex12_arq.txt:'
        f'\n-> {amount_chars}'
        '\nAmount of rows in ex12_arq.txt:'
        f'\n-> {amount_rows}'
        '\nAmount of each letter in ex12_arq.txt:'
        f'\n-> {amount_each_letter}'
    )


if __name__ == '__main__':
    main()
