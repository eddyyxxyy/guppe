"""
7) Faça uma função que receba uma temperatura en graus Celsius e retorne-a
convertida em graus Fahrenheit. A fórmula de conversão é: F = C * (9.0/5.0) + 32.0,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""
from locale import setlocale, LC_ALL, atof

from exercicios.secao08 import temp_converter


def get_float(name: str):
    while True:
        try:
            value = atof(
                input(f'Enter {name}:\n-> ')
            )
            return value
        except ValueError:
            print(f'\033[31mINVALID {name}! Try again...\033[m\n')


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    print('TEMPERATURE CONVERTER'.center(24))
    temp = get_float('temperature in Cº')
    converted_temp = temp_converter.c2f(temp)
    print(
        '\nTemperature:'
        f'\n-> {temp:n}Cº'
        '\nConverted to Fahrenheit:'
        f'\n-> {converted_temp:n}Fº'
    )


if __name__ == '__main__':
    main()
