"""
26) Faça um algoritmo que receba um número inteiro positivo n e calcule o
somatório de 1 até n.
"""


def get_int(prompt: str, positive: bool) -> int:
    while True:
        try:
            number = int(input(prompt).strip())
            if positive:
                if number < 1:
                    raise ValueError
            return number
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def sum_one_to_n(n: int) -> int:
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


def main() -> None:
    print(sum_one_to_n(get_int('Enter integer:\n-> ', False)))


if __name__ == '__main__':
    main()
