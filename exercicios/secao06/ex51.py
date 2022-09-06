"""
51) Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais.
Em 1996 recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem
ao dobro do ano anterior. Faça programa que determine o salário atual do funcionário.
"""
from datetime import date


def calc_salary():
    initial: float = 2000
    perc: float = 0.015
    salary1 = initial + (initial * perc)
    year = 1997
    todays_year = date.today().year
    while year <= todays_year:
        salary1 = salary1 + (salary1 * (perc * 2))
        year += 1
    return salary1


def main():
    salary = calc_salary()
    print(
        'Startint with a R$2000,00 salary in 1996 until now with fees:'
        f'\n-> R${salary:.2f}'.replace('.', ',')
    )


if __name__ == '__main__':
    main()
