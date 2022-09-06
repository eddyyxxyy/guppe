"""
50) Chico tem 1.50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1.10
metros e cresce 3 centímetros por ano. Escreva um programa que calcule e imprima
quantos anos serão necessários para que Zé seja maior que Chico.
"""


def calc_height() -> tuple:
    chico: float = 1.50
    ze: float = 1.10
    contador: int = 0
    while True:
        if ze >= chico:
            break
        chico += 0.02
        ze += 0.03
        contador += 1
    return chico, ze, contador


def main() -> None:
    height = calc_height()
    print(
        f'After {height[2]} years:'
        f"\nChico's height: {height[0]:.2f}"
        f"\nZé's height: {height[1]:.2f}"
    )


if __name__ == '__main__':
    main()
