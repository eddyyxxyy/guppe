"""
2) Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a
na tela no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir:
1 de janeiro de 2000.
"""
from datetime import date
from locale import LC_ALL, setlocale


def this_day() -> str:
    """
    Returns the current day, month and year of your os
    according to your locale in str

    :return: '<day> of <month> of <year>' -> str
    """
    now = date.today()
    return now.strftime('%d de %B de %Y')


def main() -> None:
    setlocale(LC_ALL, '')
    today = this_day()
    print(today)


if __name__ == '__main__':
    main()
