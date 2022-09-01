"""
19) Escreva um algoritmo que leia um número inteiro entre 100 e 999
e imprima na saída cada um dos algarismos que compõem o número
"""
from locale import atoi, format_string


def input_integer(msg: str = 'Enter a number:\n-> ') -> int:
    while True:
        try:
            number = atoi(input(msg).strip())
            return number
        except ValueError:
            print('ERROR! Try again...\n')


def main():
    print('\033[37mDigits of n\033[m\n')
    while True:
        number: int = input_integer()
        if 100 <= number <= 999:
            break
        else:
            print('Input must be between 100 and 999...\n')
    figures = [int(num) for num in str(number)]
    formmated_figures = ", ".join(
        format_string('"%d"', x) for x in figures
    )
    print(
        f'\nEach digit in {number}:'
        f'\n-> {formmated_figures}.'
    )


if __name__ == '__main__':
    main()
