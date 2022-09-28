"""
64) Implemente a função a qual recebe duas strings, str1 e str2, e
concatena a string apontada por str2 à string apontada por str1
"""


def concatenate_string(string0, string1):
    return string0 + string1


def main() -> None:
    string0 = 'Eu gosto muito de '
    string1 = 'programar em Python e SQL!'
    string_0_1 = concatenate_string(string0, string1)
    print(string_0_1)


if __name__ == '__main__':
    main()
