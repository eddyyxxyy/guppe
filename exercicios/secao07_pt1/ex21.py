"""
21) Faça um programa que receba do usuário dois vetores, A e B,
com 10 números inteiros cada. Crie um novo vetor denominado C
calculando C = A - B. Mostre na tela os dados do vetor C
"""
from collections import deque
from collections.abc import Iterator
from locale import LC_ALL, atoi, format_string, setlocale


def get_array(n: int, name: str) -> Iterator[int]:
    for i in range(n):
        while True:
            try:
                number = atoi(
                    input(f'Enter the {i + 1}º number for array {name}:\n-> ')
                )
                yield number
                break
            except ValueError:
                print('Invalid number! Try again...\n')


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a = tuple(get_array(10, 'A'))
    print()
    b = tuple(get_array(10, 'B'))
    c = deque()
    for i in range(10):
        c.append(a[i] - b[i])
    formatted_a = ', '.join(format_string('%d', x) for x in a)
    formatted_b = ', '.join(format_string('%d', x) for x in b)
    formatted_c = ', '.join(format_string('%d', x) for x in c)
    print(
        '\nArrays:'
        f'\nA -> {formatted_a}.'
        f'\nB -> {formatted_b}.'
        f'\nC (A - B) -> {formatted_c}.'
    )


if __name__ == '__main__':
    main()
