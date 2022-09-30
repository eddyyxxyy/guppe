"""
11) Faça um programa no qual o usuário informa o nome do arquivo e uma palavra,
e retorne o número de vezes que aquela palavra aparece no arquivo.
"""


def count_word(path: str, word: str) -> int:
    with open(path) as f:
        return f.read().count(word)


def main() -> None:
    result = count_word('arquivos/ex11_arq.txt', 'arquivo')
    print(f'Amount of times that the word "arquivo" was found: {result}')


if __name__ == '__main__':
    main()
