"""
13) Gere matriz 4 x 4 com valores no intervalo [1, 20]. Escreva um programa que transforme
a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os
elementos acima da diagonal principal. Imprima a matriz original e a matriz transformada.
"""
from locale import atof, setlocale, LC_ALL

from numpy import asarray, tril


def get_float_array(rows: int, columns: int) -> list[list]:
    array = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    value = atof(
                        input(f'Enter no. for [{i},{j}]:\n-> ')
                    )
                    if value < 1 or value > 20:
                        raise ValueError
                    break
                except ValueError:
                    print('\033[31mINVALID NUMBER! Try again...\033[m\n')
            row.append(value)
        array.append(row)
    return array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array = get_float_array(4, 4)
    array = asarray(array)
    print(
        '\nArray:\n' + str(array),
        '\n\nLower triangle matrix of Array:\n' + str(tril(array))
    )


if __name__ == '__main__':
    main()
