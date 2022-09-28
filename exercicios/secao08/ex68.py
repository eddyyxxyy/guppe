"""
68) Faça uma função que receba duas string e retorne a intercalação letra a letra
da primeira com a segunda string. A string intercalada deve ser retornada na primeira string
"""


def intercalate(string1, string2) -> str:
    return ''.join(map(''.join, zip(string1, string2)))


def main() -> None:
    string1 = 'abcde'
    string2 = 'fghij'
    result = intercalate(string1, string2)
    print(result)


if __name__ == '__main__':
    main()
