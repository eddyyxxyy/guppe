"""
15) Crie um programa que receba três valores (obrigatoriamente maiores que zero),
representando as medidas dos três lados de um triângulo. Elabore funções para:
(a) Determimnar se eles lados formam um triângulo, sabendo que:
    . O comprimento de cada lado de um triângulo é menor do que a soma dos outros
    dois lados.
(b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um
triângulo. Sendo que:
    . Chama-se equilátero o triângulo que tem três lados iguais.
    . Denominam-se isósceles o triângulo que tem o comprimento
    de dois lados iguais
    . Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""
from locale import setlocale, LC_ALL

from exercicios.secao08.ex09 import get_float


def check_triangle(a, b, c) -> str:
    a, b, c = sorted([a, b, c])
    if a + b <= c:
        return 'Impossible'
    if a != b != c:
        return 'Scalene'
    elif a == c:
        return 'Equilateral'
    else:
        return 'Isosceles'


def main() -> None:
    setlocale(LC_ALL, '')
    a = get_float('lenght of "a"', only_positive=True)
    b = get_float('lenght of "b"', only_positive=True)
    c = get_float('lenght of "c"', only_positive=True)
    print(f'({a:n}, {b:n}, {c:n}) is a {check_triangle(a, b, c)} triangle!')


if __name__ == '__main__':
    main()
