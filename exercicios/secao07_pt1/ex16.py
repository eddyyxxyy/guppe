"""
16) Faça um programa que leia um vetor de 5 posições para números reais e,
depois, um código inteiro, Se o código for zero, finalize o programa;
se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem
inversa. Caso, o código for diferente de 1 e 2 escreva uma mensagem informando
que o código é inválido
"""
from collections import deque
from collections.abc import Iterator
from locale import LC_ALL, atof, atoi, format_string, setlocale


def get_values(n: int) -> Iterator[float]:
    """
    Input n floats and yields the value n times
    :param n: amount of iterations to yield float values
    :return: Iterator with floats
    """
    for i in range(n):
        while True:
            try:
                number = atof(input(f'Enter {i + 1}º number:\n-> '))
                yield number
                break
            except ValueError:
                print('Invalid number! Try again...\n')


def get_code():
    while True:
        try:
            code = atoi(
                input(
                    '\nEnter the code:'
                    '\n0 - Shutdown program;'
                    '\n1 - Show numbers;'
                    '\n2 - Show numbers in reverse;'
                    '\n-> '
                )
            )
            if code < 0 or code > 2:
                raise ValueError
            return code
        except ValueError:
            print('Invalid code! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = deque(get_values(5))
    formatted_numbers = ', '.join(format_string('%d', x) for x in numbers)
    code = get_code()
    if code == 0:
        exit('\nShutting down!')
    if code == 1:
        print('\nNumbers:' f'\n-> {formatted_numbers}.')
    if code == 2:
        numbers.reverse()
        formatted_numbers_reverse = ', '.join(
            format_string('%d', x) for x in numbers
        )
        print('\nReversed Numbers:' f'\n-> {formatted_numbers_reverse}.')


if __name__ == '__main__':
    main()
