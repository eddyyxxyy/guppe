"""
60) Escreva uma função que retorne a primeira posição de uma sub-string
dentro de uma string. Caso a sub-string não seja encontrada, a função
deve retornar -1.
"""


def find_substring(string: str, substring: str) -> int:
    return string.lower().find(substring)


def main() -> None:
    string0 = 'Eu bebo vinho'
    substring0 = 'vinho'
    print(find_substring(string0, substring0))


if __name__ == '__main__':
    main()
