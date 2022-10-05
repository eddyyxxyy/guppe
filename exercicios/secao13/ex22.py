"""
22) Faça um programa que recebe como entrada o nome de um arquivo de
entrada e o nome de um arquivo saída. O arquivo de entrada contém
o nome de um aluno ocupando 40 caracteres e três inteiros que indicam
suas notas. O programa deverá ler o arquivo de entrada e gerar um arquivo
de saída onde aparece o nome do aluno e as suas notas em ordem crescente.
"""
import sys

from pathvalidate import validate_filename, ValidationError


def check_name(file_name):
    try:
        validate_filename(file_name)
        return True
    except ValidationError as e:
        print(f"{e}\n", file=sys.stderr)
        return False


def main() -> None:
    read_file = str(input('Enter the file to be read: '))
    new_file = str(input('Enter the file name to be created: '))
    if check_name(read_file) and check_name(new_file):
        with open('arquivos/' + read_file) as f0, \
                open('arquivos/' + new_file, 'w') as f1:
            student = [f0.read(40), sorted([int(grade) for grade in f0.read().split()])]
            f1.write(student[0].ljust(40) + str(student[1]))


if __name__ == '__main__':
    main()
