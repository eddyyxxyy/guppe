"""
19) Faça um programa que receba do usuário um arquivo que contenha o nome
e a nota de diversos alunos.txt (da seguinte forma: NOME:JOÃO NOTA:8), um aluno
por linha. Mostre na tela o nome e a nota do aluno que possui a maior nota.
"""


def main() -> None:
    with open('arquivos/ex19_students.txt') as f:
        students = []
        result = ['', 0]
        for student in f:
            students.append(student.split())
        for student in range(len(students)):
            if float(students[student][-1].split(':')[-1]) > float(result[1]):
                result = [students[student][0].split(":")[-1], students[student][-1].split(':')[-1]]
        print(f'Student: {result[0]} | Grade: {result[1]}')


if __name__ == '__main__':
    main()
