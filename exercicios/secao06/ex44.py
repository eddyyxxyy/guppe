"""
44) Leia um número positivo do usuário, então, calcule e imprima a
sequência Fibonacci até o primeiro número superior lido. Exemplo:
se o usuário informou o número 30, asequência a ser impressa será
0 1 1 2 3 5 8 13 21 34.
"""
from collections.abc import Iterator
from locale import atoi


def get_positive_int(msg: str = 'Enter a integer:\n-> ') -> int:
    while True:
        try:
            number: int = atoi(input(msg).strip())
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def fibonacci_sequence() -> Iterator[int]:
    stop = get_positive_int()
    a, b = 0, 1
    for i in range(stop):
        yield a
        if a > stop:
            break
        a, b = b, a + b


def main() -> None:
    numbers = tuple(fibonacci_sequence())
    print(numbers)


if __name__ == '__main__':
    main()
