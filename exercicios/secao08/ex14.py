"""
14) Faça uma função que receba a distância em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em km/l e escreva uma mensagem
de acordo com a tabela abaixo:
    | CONSUMO    | (km/l)  | MENSAGEM
    | menor que  |   8     | Venda o carro!
    | entre      | 8 e 12  | Econômico
    | maior que  |  12     | Super econômico!
"""
from locale import LC_ALL, setlocale

from exercicios.secao08.ex09 import get_float


def km_per_l(km: float, lc: float) -> str:
    result = km / lc
    if result < 8:
        return 'Sell that car!'
    if 8 <= result <= 12:
        return 'Econimic car!'
    if result > 12:
        return 'SUPER Economic car!'


def main() -> None:
    setlocale(LC_ALL, '')
    km = get_float('the distance in km')
    lc = get_float('the gasoline consumed')
    print(km_per_l(km, lc))


if __name__ == '__main__':
    main()
