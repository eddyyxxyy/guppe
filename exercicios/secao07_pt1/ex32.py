"""
32) Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma
que o usuário não informa elementos repetidos). Calcule e mostre os
vetores resultantes em cada caso abaixo:
    . Soma entre x e y: soma de cada elemento x com o elemento da mesma
    posição em y.
    . Produto entre x e y: multiplicação de cada elemento de x com o
    elemento da mesma posição em y.
    . Diferença entre x e y: todos os elementos de x que não existam em y.
    . Interseção entre x e y: apenas os elementos que aparecem nos dois vetores
    . União entre x e y: todos os elemntos de x, e todos os elementos de y
    que não estão em x.
"""
from collections import deque
from locale import LC_ALL, atoi, format_string, setlocale
from operator import add, mul


def get_non_repeated_ints(n: int, name: str) -> deque[int]:
    numbers = deque()
    for i in range(n):
        while True:
            try:
                numbers.append(
                    atoi(input(f'Enter the {i + 1}º number of {name}:\n-> '))
                )
                break
            except ValueError:
                print('Invalid number! Try again...')
    return numbers


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    x: deque = get_non_repeated_ints(5, 'x')
    print()
    y: deque = get_non_repeated_ints(5, 'y')
    print(
        '\nx:' '\n->',
        ', '.join(format_string('%d', x) for x in x) + '\ny:' '\n->',
        ', '.join(format_string('%d', x) for x in y) + '\nSum between x and y:'
        f'\n->',
        ', '.join(format_string('%d', x) for x in map(add, x, y))
        + '\nMultiplication between x and y:'
        f'\n->',
        ', '.join(format_string('%d', x) for x in map(mul, x, y))
        + '\nDifference of x and y:'
        f'\n->',
        ', '.join(format_string('%d', x) for x in set(x).difference(y))
        + '\nIntersection of x and y:'
        f'\n->',
        ', '.join(format_string('%d', x) for x in set(x).intersection(y))
        + '\nUnion of x and y:'
        f'\n->',
        ', '.join(format_string('%d', x) for x in set(x).union(y)),
    )


if __name__ == '__main__':
    main()
