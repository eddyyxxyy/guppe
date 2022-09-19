"""
17) Faça uma função que receba dois números inteiros positivos
por parâmetro e retorne a soma dos N números inteiros existentes
entre eles.
"""
from locale import atoi, setlocale, LC_ALL, format_string


def n_between(a: int, b: int) -> tuple[int, set] | str:
    result = set()
    if a != b:
        if a < b:
            for value in range(a + 1, b):
                result.add(value)
            return sum(result), result
        else:
            for value in range(b + 1, a):
                result.add(value)
            return sum(result), result
    else:
        return f'There are no numbers between {a:n} and {b:n}.'


def get_positive_int(name: str) -> int:
    while True:
        try:
            number = atoi(
                input(f'Enter no. (integer) for "{name}":\n-> ')
            )
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def main() -> None:
    setlocale(LC_ALL, '')
    a = get_positive_int('A')
    b = get_positive_int('B')
    values_between = n_between(a, b)
    formatted_values = ', '.join(
        format_string('%d', x) for x in values_between[1]
    )
    print(
        '\nNumbers:'
        f'\n-> {formatted_values}.'
        '\nSum of Numbers:'
        f'\n-> {sum(values_between[1]):n}'
    )


if __name__ == '__main__':
    main()
