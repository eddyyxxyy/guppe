"""
27) Faça uma função que receba como parâmetro o valor de um ângulo em
graus e calcule o valor do seno desse ângulo usando sua respectiva serie de Taylor:
sin x = E (n = 0) = (-1) ^ n  / (2n + 1)! * x ^ 2n + 1 = x - (x ^ 3 / 3!) + (x ^ 5 / 5!) - ...
para tod0 x, onde x é o valor do ângulo em radianos. Considerar r = 3.141593 e n variando
de 0 até 5
"""
from math import factorial, radians


def get_degrees(prompt: str):
    while True:
        try:
            angle = float(input(prompt))
            if angle < 0:
                raise ValueError
            return angle
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def senx(x, n):
    x = radians(x)

    def termo_geral(x, i):
        return ((-1) ** i / factorial(2 * i + 1)) * (x ** (2 * i + 1))

    def termos(x, n):
        for i in range(n):
            yield termo_geral(x, i)

    return sum(termos(x, n))


def main() -> None:
    result = senx(
        x=get_degrees('Enter size in degrees for the angle:\n-> '), n=6
    )
    print(result)


if __name__ == '__main__':
    main()
