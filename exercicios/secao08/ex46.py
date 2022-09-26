"""
46) Crie um programa contendo as seguintes funcões que recebem um vetor V
números reais como parâmetros:
. Impressão normal do vetor.
. Impressão inversa.
. Função que retorna a média aritmética dos elementos do vetor.
"""
from random import sample
from statistics import mean


def print_array(v: list):
    print(v)


def print_inverted_array(v: list):
    print(v[::-1])


def print_mean_array(v: list):
    print(mean(v))


def main() -> None:
    array = sample(range(1, 101), 5)
    print_array(array)
    print_inverted_array(array)
    print_mean_array(array)


if __name__ == '__main__':
    main()
