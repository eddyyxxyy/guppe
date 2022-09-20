"""
11) Elabore uma função que receba três notas de um aluno como parâmetros e
uma letra. Se a letra for A, a função deverá calcular a média aritmética das
notas do aluno; se for P, deverá calcular a média ponderada, com pesos 5, 3, e 2.
"""
from locale import LC_ALL, setlocale

from exercicios.secao08.ex09 import get_float


def grade_averages(*args: float, op: str) -> float:
    values = args
    if op == 'a':
        return sum(args) / len(args)
    elif op == 'p':
        result = values[0] * 5, values[1] * 3, values[2] * 2
        return sum(result) / 10


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    grade1 = get_float('grade')
    grade2 = get_float('grade')
    grade3 = get_float('grade')
    grades = grade_averages(grade1, grade2, grade3, op='p')
    print(grades)


if __name__ == '__main__':
    main()
