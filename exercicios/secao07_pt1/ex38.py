"""
38) Peça ao usuário para digitar dez valores numéricos e ordene por ordem
crescente esses valores, guardando-os num vetor. Ordene o valor assim
que ele for digitado. Mostre ao final na tela os valores em ordem.
"""
from locale import LC_ALL, atof, format_string, setlocale


def get_floats(n: int) -> list[float]:
    """
    Yields n floats to an Iterator
    :param n: int
    :return: Iterator[float]
    """
    numbers = []
    for i in range(n):
        while True:
            try:
                number = atof(input(f'Enter the {i + 1}º number:\n-> '))
                numbers.append(number)
                numbers.sort()
                break
            except ValueError:
                print('Invalid grade value! Try again...\n')
    return numbers


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a = get_floats(10)
    print(
        '\nArray "A":' f'\n->',
        ', '.join(format_string('%.1f', x) for x in a),
        end='.',
    )


if __name__ == '__main__':
    main()
