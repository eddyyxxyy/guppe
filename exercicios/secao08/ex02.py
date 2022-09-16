"""
2) Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a
na tela no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir:
1 de janeiro de 2000.
"""
from datetime import date
from locale import setlocale, LC_ALL


def this_day() -> str:
    now = date.today()
    return now.strftime('%d de %B de %Y')


def main() -> None:
    setlocale(LC_ALL, '')
    today = this_day()
    print(today)


if __name__ == '__main__':
    main()
