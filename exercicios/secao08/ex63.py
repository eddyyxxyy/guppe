"""
63) Crie uma função que compara duas string e que retorna se elas
são iguais ou diferentes
"""


def string_comp(string_a, string_b):
    return True if string_a == string_b else False


def main() -> None:
    string0 = 'Eu não acho legal mexer com strings'
    string1 = 'Eu não acho legal mexer com strings'
    string2 = 'Eu adoro mexer com strings'
    string3 = 'Eu amo mexer com strings'
    print(string_comp(string0, string1))
    print(string_comp(string2, string3))


if __name__ == '__main__':
    main()
