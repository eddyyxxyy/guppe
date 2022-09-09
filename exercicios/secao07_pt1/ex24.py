"""
24) Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura
em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número do
aluno mais baixo e do mais alto, juntamente com suas alturas.
"""
from collections.abc import Iterator
from locale import setlocale, LC_ALL, atoi, atof


def get_student(n: int) -> Iterator[dict]:
    for i in range(n):
        while True:
            try:
                student_id = atoi(
                    input(f'Enter the Id for the {i + 1}º student:\n-> ')
                )
                if student_id < 0:
                    raise ValueError
                break
            except ValueError:
                print('Invalid Id! Try again...\n')
        while True:
            try:
                student_height = atof(
                    input(f'Enter the height for the {i + 1}º student:\n-> ')
                )
                if student_height < 0.5 or student_height > 2.45:
                    raise ValueError
                break
            except ValueError:
                print('Invalid height! Try again...\n')
        yield student_id, student_height


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    students = tuple(get_student(10))
    shortest_student = (None, 2.4)
    biggest_student = (None, 0)
    for student, height in students:
        if height < shortest_student[1]:
            shortest_student = (student, height)
        if height > biggest_student[1]:
            biggest_student = (student, height)
    print(
        '\nSmallest Student:'
        f'\n-> Id: {shortest_student[0]} | Height: {shortest_student[1]}'
        '\nBiggest Student:'
        f'\n-> Id: {biggest_student[0]} | Height: {biggest_student[1]}'
    )


if __name__ == '__main__':
    main()
