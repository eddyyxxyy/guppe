"""
3) Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado
das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
10 elementos cada. Imprimir todos os conjuntos.
"""
from collections import deque
from locale import atof, setlocale, LC_NUMERIC, format_string


def get_num(msg: str) -> float:
    while True:
        try:
            number = atof(input(msg))
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def main() -> None:
    setlocale(LC_NUMERIC, 'pt-BR')
    numbers = deque()
    sqr = deque()
    for i in range(10):
        numbers.append(
            get_num('Enter a number:\n-> ')
        )
        sqr.append(numbers[i] ** 2)
    formated_numbers = ' - '.join(
        format_string('%.1f', x) for x in numbers
    )
    formated_sqr = ' - '.join(
        format_string('%.1f', x) for x in sqr
    )
    print(
        '\nList of numbers:'
        f'\n-> {formated_numbers}.'
        '\nList of squares of numbers:'
        f'\n-> {formated_sqr}.'
    )


if __name__ == '__main__':
    main()

"""
lista1 = []
lista2 = []
for i in range(10):
    lista1.append(float(input(f'Informe um valor para a posição {i}: ')))
    lista2.append(lista1[i] * 2)
print(lista1)
print(lista2)
"""
