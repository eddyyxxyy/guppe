"""
22) Crie uma função que receba parâmetro um valor inteiro e gere como
saída n linhas com pontos de exclamação, conforme o exemplo abaixo (para n = 5):
    !
    !!
    !!!
    !!!!
    !!!!!
"""

from locale import LC_ALL, atoi, setlocale


def get_int(prompt: str, only_posit: bool = False) -> int:
    while True:
        try:
            number = atoi(input(prompt))
            if only_posit:
                if number < 0:
                    raise ValueError
            return number
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def exclamation_lines(lines: int) -> str:
    result_string: str = ''
    for line in range(1, lines + 1):
        result_string += ('!' * line) + '\n'
    return result_string


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    lines = get_int(prompt='Enter no. of lines:\n-> ', only_posit=True)
    string = exclamation_lines(lines)
    print(string)


if __name__ == '__main__':
    main()
