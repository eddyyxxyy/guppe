"""
66) Faça uma função que dado um caractere qualquer retorne o mesmo
caractere sempre em maiúsculo.
"""


def upper_char(char):
    return char.upper()


def main() -> None:
    char = 'a'
    print(upper_char(char))


if __name__ == '__main__':
    main()
