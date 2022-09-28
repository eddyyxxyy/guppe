"""
62) Crie uma função que calcule o comprimento de uma string.
"""


def lenght(string0):
    result = 0
    for _ in string0:
        result += 1
    return result


def main() -> None:
    string0 = 'Eu realmente gosto de mexer com strings!'
    print(lenght(string0))


if __name__ == '__main__':
    main()
