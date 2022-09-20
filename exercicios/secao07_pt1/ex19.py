"""
19) Faça um vetor de tamanho 50 preenchido com o seguinte valor:
(i + 5 * i) % (i + 1), sendo i a posição do elemento no vetor.
Em seguida imprima o vetor na tela.
"""
from collections import deque
from locale import LC_ALL, format_string, setlocale


def array_50_i() -> str:
    numbers = deque()
    for i in range(50):
        numbers.append((i + 5 * i) % (i + 1))
    formatted_numbers = ', '.join(format_string('%d', x) for x in numbers)
    return formatted_numbers


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = array_50_i()
    print('Numbers:' f'\n-> {numbers}.')


if __name__ == '__main__':
    main()
