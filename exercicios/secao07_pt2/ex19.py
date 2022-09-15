"""
19) Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo
as seguintes informações sobre alunos de uma disciplina, sendo todas as informações do
tipo inteiro:
    . Primeira coluna: número de matrícula (use um inteiro)
    . Segunda coluna: média das provas
    . Terceira coluna: média dos trabalhos
    . Quarta coluna: nota final
(a) Leia as três primeiras informações de cada aluno.
(b) Calcule a nota final como sendo a soma da média das provas e da média
dos trabalhos.
(c) Imprima a matrícula do aluno que obteve a maior nota final (assuma que
só existe uma maior nota).
(d) Imprima a média aritmética das notas finais.
"""
from locale import setlocale, LC_ALL, atoi, atof


def get_int(prompt: str) -> int:
    while True:
        try:
            value = atoi(
                input(prompt)
            )
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def get_float(prompt: str) -> float:
    while True:
        try:
            value = atof(
                input(prompt)
            )
            if value < 0 or value > 10:
                raise ValueError
            return value
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array = []
    best_studant = []
    arithmetic_average = 0
    for i in range(5):
        row = []
        for j in range(1):
            row.append(get_int(f'Enter {i + 1}ª studant id:\n-> '))
            row.append(get_float(f'Enter {i + 1}ª studant grade average of tests:\n-> '))
            row.append(get_float(f'Enter {i + 1}ª studant grade average of extra activities:\n-> '))
            row.append(row[1] + row[2])
            arithmetic_average += row[1] + row[2]
            if i == 0:
                best_studant.append(row[0])
                best_studant.append(row[3])
            else:
                if row[3] > best_studant[1]:
                    best_studant[0] = row[0]
                    best_studant[1] = row[3]
        array.append(row)
    for index, studant in enumerate(array):
        print(
            f'\n{index + 1}º studant:'
            '\n-> Id:', studant[0],
            '\n-> Grade average of tests:', studant[1],
            '\n-> Grade average of extras:', studant[2],
            '\n-> Final grade:', studant[3]
        )
    print(
        '\n\nBest studant:',
        f'\n-> id: {best_studant[0]}',
        f'\n-> Final grade: {best_studant[1]}.',
        f'\n\nArithmetic average of all studants:',
        f'\n-> {arithmetic_average / 5:n}.'
    )


if __name__ == '__main__':
    main()
