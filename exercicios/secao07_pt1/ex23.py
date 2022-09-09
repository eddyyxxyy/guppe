"""
23) Ler dois conjuntos de números reais, armazenando-os em vetores
e calcular o produto escalar entre eles. Os conjuntos têm 5 elementos
cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto
escalar é dado por: x1 * y1 + x2 * y2 + ... + xn * yn
"""
from collections.abc import Iterator
from locale import setlocale, LC_ALL, atof, format_string


def get_float_array(n: int, name: str) -> Iterator[float]:
    for i in range(n):
        while True:
            try:
                number = atof(
                    input(f'Enter the {i + 1}º number for array "{name}":\n-> ')
                )
                yield number
                break
            except ValueError:
                print('Invalid number! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array_a = tuple(get_float_array(5, 'A'))
    print()
    array_b = tuple(get_float_array(5, 'A'))
    formatted_array_a = ', '.join(
        format_string('%.1f', x) for x in array_a
    )
    formatted_array_b = ', '.join(
        format_string('%.1f', x) for x in array_b
    )
    result: float = 0
    for i in range(5):
        result += array_a[i] * array_b[i]
    print(
        '\nArrays:'
        f'\nA -> {formatted_array_a}.'
        f'\nB -> {formatted_array_b}.'
        '\nDot product:'
        f'\nProduct -> {result:n}'
    )


if __name__ == '__main__':
    main()
