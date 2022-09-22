"""
31) Faça uma função para calcular o número neperiano usando uma série.
A função deve ter como parâmetro o número de termos que serão somados
(note que, quannto maior o número, mais próxima a resposta estará do valor e).
l = E(n=0) = 1 / n! = 1 / 0! + 1 / 1! + 1 / 2! + 1 / 3!
"""
from math import factorial


def neperian_num(terms: int) -> float:
    result = 0
    for i in range(terms + 1):
        result += 1 / factorial(i)
    return result


def main() -> None:
    while True:
        try:
            number = int(input('Enter integer:\n-> '))
            break
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')
    print(neperian_num(number))


if __name__ == '__main__':
    main()
