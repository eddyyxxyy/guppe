"""
17) Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em
seguida, escreva o número de alunos cuja pior nota foi na prova 1, o número
de alunos cuja pior nota foi na prova 2, e o número de alunos cuja pior
nota foi na prova 3. Em caso de empate das piores notas de um aluno,
o critério de desempate é arbitrário, mas o aluno
deve ser contabilizado apenas uma vez.
"""
from locale import setlocale, LC_ALL, atof

from numpy import asarray


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
                    if value < 0 or value > 10:
                        raise ValueError
                    break
                except ValueError:
                    print('\033[31mINVALID NUMBER! Try again...\033[m\n')
            row.append(value)
        array.append(row)
    return array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array = get_float_array(5, 3)
    test1 = 0
    test2 = 0
    test3 = 0
    for row in array:
        if min(row) is row[0]:
            test1 += 1
        elif min(row) is row[1]:
            test2 += 1
        else:
            test3 += 1
    print('\nArray:\n' + str(asarray(array)))
    print('\nWorst grades in test 1:', test1)
    print('\nWorst grades in test 2:', test2)
    print('\nWorst grades in test 3:', test3)


if __name__ == '__main__':
    main()
