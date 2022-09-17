"""
9) Faça uma função que receba a altura e o raio de um cilindro circular e
retorne o volume do cilindro. O volume de um cilindro circular é calculado por meio
da seguinte fórmula: V = pi * (raio ** 2) * altura, onde r = 3.141592
"""
from locale import atof, setlocale, LC_ALL

from numpy import pi


def cylinder_vol(h: float, r: float) -> float:
    return pi * (r ** 2) * h


def get_float(name: str, only_positive: bool = False) -> float:
    while True:
        try:
            value = atof(
                input(f'Enter {name}:\n-> ')
            )
            if only_positive:
                if value <= 0:
                    raise ValueError
            return value
        except ValueError:
            print(f'\033[31mINVALID {name.upper()}! Try again...\033[m\n')


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    h = get_float('height of the cylinder', True)
    r = get_float('radius of the cylinder', True)
    volume = cylinder_vol(h, r)
    print(
        '\nVolume of a cylinder:'
        f'\n-> {volume:n}³ = {pi:n} * ({r:n} ** 2) * {h:n}'
    )


if __name__ == '__main__':
    main()
