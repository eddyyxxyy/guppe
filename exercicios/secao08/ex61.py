"""
61) Escreva uma função que compare e retorne verdadeiro, caso uma string
seja anagrama da outra, e falso, caso contrario.
"""


def anagramn(string0, string1):
    flag = False
    string0 = sorted(string0)
    string1 = sorted(string1)
    if string0 == string1:
        flag = True
    return flag


def main() -> None:
    string0 = 'roma'
    string1 = 'amor'
    string2 = 'agua'
    string3 = 'calor'
    print(anagramn(string0, string1))
    print(anagramn(string2, string3))


if __name__ == '__main__':
    main()
