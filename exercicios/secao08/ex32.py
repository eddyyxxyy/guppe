"""
32) Faça uma funçao chamada 'simplifica' que recebe como parâmetro o numerador
e o denominador de uma fração. Esta função deve simplificar a fração
recebebida dividindo o numero e o denominador pelo maior fator possível.
Por exemplo, a fração 36/60 simplifica para 3/5 dividindo o numerador e o denominador
por 12. A funcão deve modificar as variáveis passadas como parâmetro.
"""


def simplify(numerator: int, denominator: int) -> tuple[int, int]:
    if denominator > 0:
        for i in range(denominator, 1, -1):
            if numerator % i == 0 and denominator % i == 0:
                numerator = int(numerator / i)
                denominator = int(denominator / i)
                break
    else:
        for i in range(denominator * (-1), 1, -1):
            if numerator % i == 0 and denominator % i == 0:
                numerator = int(numerator / i)
                denominator = int(denominator / i)
                break
    return numerator, denominator


def main() -> None:
    result = simplify(360, 400)
    print(f'{result[0]}/{result[1]}')


if __name__ == '__main__':
    main()
