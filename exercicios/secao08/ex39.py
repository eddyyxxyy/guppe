"""
39) Faça uma função 'Troque', que recebe duas variáveis reais A e B
e troca o valor delas (i.e., A recebe o valor de B e B recebe o valor de A).
"""


def swap(a: float, b: float) -> tuple:
    a, b = b, a
    return a, b


def get_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def main() -> None:
    a = get_float('Enter number for "a": ')
    b = get_float('Enter number for "b": ')
    swap_a_b = swap(a, b)
    print(
        f'\nSwap of a ({a}) and b ({b}):'
        f'\n-> a = {swap_a_b[0]}'
        f'\n-> b = {swap_a_b[1]}'
    )


if __name__ == '__main__':
    main()
