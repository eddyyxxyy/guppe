"""
22) Escreva um programa completo que permita a qualquer aluno
introduzir, pelo teclado, uma sequência arbitrária de notas(válidas no intervalo de
10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética.
O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido
ao programa, o qual terminará quando for introduzido um valor que não seja válido
como nota de aprovação.
"""
from collections.abc import Iterator
from locale import atof


def get_grades(msg: str = 'Enter your grade (from 10 to 20):\n-> ') -> Iterator[float]:
    while True:
        try:
            grade = atof(input(msg).strip())
            if grade < 10 or grade > 20:
                break
            yield grade
        except ValueError:
            print('Invalid grade! Try again...\n')


def arithmetic_average() -> float:
    grades = tuple(get_grades())
    return sum(grades) / len(grades)


def main() -> None:
    arithmetic_result = arithmetic_average()
    print(
        '\nArithmetic Average:'
        f'\n-> {arithmetic_result:.2f}'
    )


if __name__ == '__main__':
    main()
