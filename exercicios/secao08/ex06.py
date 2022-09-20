"""
6) Faça uma função que receba 3 números inteiros como parâmetro,
representando horas, minutos e segundos, e os converta em segundos
"""
from datetime import datetime, time
from locale import LC_ALL, atoi, setlocale


def get_int(limit: int, name: str):
    while True:
        try:
            value = atoi(input(f'Enter {name}:\n->'))
            if value > limit:
                raise ValueError
            return value
        except ValueError:
            print(f'\033[31mINVALID {name.upper()}! Try again...\033[m\n')


def time_to_seconds() -> tuple:
    """
    Takes in hours, minutes and seconds and return the
    total of seconds that time has.

    :return: tuple[time, total_of_seconds]
    """
    t = time(
        get_int(24, 'hours'), get_int(60, 'minutes'), get_int(60, 'seconds')
    )
    return (
        t,
        (datetime.combine(datetime.min, t) - datetime.min).total_seconds(),
    )


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    t = time_to_seconds()
    print('\nTime:', t[0], '\nTime to seconds:', t[1])


if __name__ == '__main__':
    main()
