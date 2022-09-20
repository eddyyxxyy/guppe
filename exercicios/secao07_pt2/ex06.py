"""
6) Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores
valores de cada posição das matrizes lidas.
"""
from locale import LC_ALL, atoi, setlocale


def get_int_array(rows: int, columns: int, name: str) -> list:
    int_array = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    value = atoi(
                        input(f'Enter no. for ({i},{j}) of "{name}":\n-> ')
                    )
                    row.append(value)
                    break
                except ValueError:
                    print('\n\033[31mINVALID! Try again...\033[m\n')
        int_array.append(row)
    return int_array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a1 = get_int_array(4, 4, 'a1')
    a2 = get_int_array(4, 4, 'a2')
    a3 = [[max(row) for row in a1], [max(row) for row in a2]]
    print('\nA1:')
    for row in a1:
        print(f'{row}')
    print('\nA2:')
    for row in a2:
        print(f'{row}')
    print('\nA3:')
    for row in a3:
        print(f'{row}')


if __name__ == '__main__':
    main()
