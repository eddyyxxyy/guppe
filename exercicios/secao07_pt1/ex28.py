"""
28) Leia 10 números inteiros e armazene em um vetor v. Crie
dois novos vetores v1 e v2. Copie os valores ímpares de v para v1,
e os valores pares de v para v2. Note que cada um dos vetores v1 e v2
têm no máximo 10 elementos, mas nem todos os elementos são utilizados.
No final escreva os elementos UTILIZADOS de v1 e v2.
"""
from collections import deque
from locale import setlocale, LC_ALL

from exercicios.secao07_pt1.ex07 import get_ints


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    v = tuple(get_ints(10))
    v1 = deque(x for x in v if x % 2 != 0)
    v2 = deque(x for x in v if x % 2 == 0)
    print(f'\nv1: {set(v1)}', f'\nv2: {set(v2)}')


if __name__ == '__main__':
    main()
