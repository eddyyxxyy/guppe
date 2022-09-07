"""
59) Escreva um programa que leia o número de habitantes de uma determinada cidade,
o valor do kwh, e para cada habitante entre com os seguintes dados: consumo do
mês e o código do consumidor (1-Residencial, 2-Comercial, 3-industrial). No final imprima
o maior, o menor e a média do consumo dos habitantes: e por fim o total do consumo de
cada categoria de consumidor.
"""
from locale import atof, LC_ALL, setlocale, currency
from collections import deque


def get_number(msg: str, limit: float = 0) -> float:
    while True:
        if limit == 0:
            try:
                number = atof(input(msg).strip())
                if number <= 0:
                    raise ValueError
                return number
            except ValueError:
                print('Invalid number! Try again...\n')
        else:
            try:
                number = atof(input(msg).strip())
                if number <= 0 or number > limit:
                    raise ValueError
                return number
            except ValueError:
                print('Invalid number! Try again...\n')


def main() -> None:
    setlocale(LC_ALL, 'pt-BR')
    print('-' * 50)
    population = get_number('Enter the city population:\n-> ')
    kwh_charge = get_number('Enter the Kw/h value:\n-> ')
    people = deque()
    consumption = deque()
    residential = deque()
    commercial = deque()
    industrial = deque()
    print(
        '-' * 50 + '\n' +
        'Inhabitant codes:'
        '\n1 - Residential'
        '\n2 - Commercial'
        '\n3 - Industrial\n'
    )
    for person in range(1, int(population) + 1):
        # Appends a tuple with monthly consumption and the inhabitant code
        people.append(
            (
                get_number(f'Enter {person:n}º inhabitant Kw/h last month consumption:\n-> '),
                get_number(f'Enter {person:n}º inhabitant code:\n-> ', limit=3)
            )
        )
    for data in people:
        if data[1] == 1:
            residential.append(data[0])
        elif data[1] == 2:
            commercial.append(data[0])
        elif data[1] == 3:
            industrial.append(data[0])
        consumption.append(data[0])
    max_consum = max(consumption)
    min_consum = min(consumption)
    average_consum = sum(consumption) / len(consumption)
    residential_consum = sum(residential) if len(residential) >= 1 else 0
    commercial_consum = sum(commercial) if len(commercial) >= 1 else 0
    industrial_consum = sum(industrial) if len(industrial) >= 1 else 0
    print(
        f'\nInformation about all the {len(people)} inhabitants:'
        f'\n-> Max consumption: {max_consum}Kw/h -> '
        f'{currency((max_consum * kwh_charge), grouping=True)}'
        f'\n-> Min consumption: {min_consum}Kw/h -> '
        f'{currency((min_consum * kwh_charge), grouping=True)}'
        f'\n-> Average consumption: {average_consum}Kw/h -> '
        f'{currency((average_consum * kwh_charge), grouping=True)}'
        '\n'
        '\nInformation about each type of consumption:'
        f'\n-> Residential: {residential_consum}Kw/h -> '
        f'{currency((residential_consum * kwh_charge), grouping=True)}'
        f'\n-> Commercial: {commercial_consum}Kw/h -> '
        f'{currency((commercial_consum * kwh_charge), grouping=True)}'
        f'\n-> Industrial: {industrial_consum}Kw/h -> '
        f'{currency((industrial_consum * kwh_charge), grouping=True)}'
    )


if __name__ == '__main__':
    main()
