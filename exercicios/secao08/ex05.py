"""
5) Faça uma função e um programa de teste para o cálculo do volume
de uma esfera. Sendo que o raio é passado por parâmetro.
V = 4/3 * pi * R³
"""
from locale import setlocale, LC_ALL, atof

from numpy import pi


def get_float(prompt: str) -> float:
    while True:
        try:
            number = atof(
                input(prompt)
            )
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def sphere_vol(r: float) -> float:
    return (4/3) * pi * (r ** 3)


def main() -> None:
    setlocale(LC_ALL, '')
    r = get_float('Enter the radius of the sphere:\n-> ')
    vol = sphere_vol(r)
    print(
        f'\nA sphere with {r:n} radius has:'
        f'\n-> {vol:n}³'
    )


if __name__ == '__main__':
    main()
