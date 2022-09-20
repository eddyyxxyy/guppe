"""
39) Faça um programa que calcule a área de um triângulo, cuja base e altura
são fornecida pelo usuário. Esse programa não pode permitir a entrada de dados inválidos,
ou seja, medidas menores ou iguais a 0.
"""
from locale import atoi


def get_positive_integer(msg: str = 'Enter a positive integer:\n-> ') -> int:
    while True:
        try:
            number: int = atoi(input(msg).strip())
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            print('Number must be an integer! Try again..')


def triangle() -> float:
    base: int = get_positive_integer(
        'Enter the value for the base of the triangle:\n-> '
    )
    height: int = get_positive_integer(
        'Enter the value for the height of the triangle:\n-> '
    )
    return (base * height) / 2


def main():
    area: float = triangle()
    print('Area:' f'\n-> {area}²')


if __name__ == '__main__':
    main()
