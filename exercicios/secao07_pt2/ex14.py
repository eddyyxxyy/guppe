"""
14) Faça um prorgrama para gerar automaticamente números entre 0 e 99 de uma
cartela de bingo. Sabendo que cada cartela deverá conter 5 linhas de 5
números, gere estes dados de modo a não ter números repetidos dentro das cartelas.
O programa deve exibir na tela a cartela gerada.
"""
from numpy.random import randint


def main() -> None:
    array = randint(100, size=(5, 5))
    print(
        'BINGO'.center(20, '-') + '\n\n' +
        'Generated card:',
        '\n' + str(array).center(18)
    )


if __name__ == '__main__':
    main()
