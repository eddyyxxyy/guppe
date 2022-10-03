"""
20) Crie um programa que receba como entrada o número de alunos de
uma disciplina. Aloque dinamicamente dois vetores para armazenar
as informações a respeito desses alunos. O primeiro vetor contém
o nome dos alunos e o segundo contém suas notas finais. Crie
um arquivo que armazene, a cada linha, o nome do aluno e sua nota
final. Use nomes com no máximo 40 caracteres. Se o nome não contém 40 caracteres,
complete com espaço em branco.
"""


def main() -> None:
    students = int(input('Number of students: '))
    with open('arquivos/ex20_arq.txt', 'a') as f:
        names = []
        grades = []
        for i in range(students):
            names.append(input(f'Enter {i + 1} students name: ').title())
            grades.append(input(f'Enter {i + 1} students grade: ') + '\n')
        result = zip(names, grades)
        for student in result:
            f.write(student[0].ljust(40) + student[1])


if __name__ == '__main__':
    main()
