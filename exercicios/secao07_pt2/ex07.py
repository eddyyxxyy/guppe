"""
7) Gerar e imprimir uma matriz de tamanho de 10 x 10, onde
seus elementos são da forma:
A[i][j] = 2i + 7j - 2 se i < j:
A[i][j] = 3i² - 1 se i = j:
A[i][j] = 4i³ - 5j² + 1 se i > j:
"""


def array(rows: int, columns: int) -> list:
    a = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if i < j:
                row.append((2 * i) + (7 * j) - 2)
            elif i == j:
                row.append(((3 * i) ** 2) - 1)
            elif i > j:
                row.append(((4 * i) ** 3) - ((5 * j) ** 2) + 1)
        a.append(row)
    return a


def main() -> None:
    for row in array(10, 10):
        print(f'{row}')


if __name__ == '__main__':
    main()
