"""
65) Implemente a função a qual recebe duas strings, str1 e str2, e um
valor inteiro positivo N. A função concatena não mais que N caractere
da string apontada por str2 à string apontada por str1 e termina str1 com NULL.
"""


def concatenate(string0, string1, num):
    return string0 + string1[:num:]


def main() -> None:
    string0 = "Ana "
    string1 = "Julia"
    num = 3
    print(f"{concatenate(string0, string1, num)}")


if __name__ == '__main__':
    main()
