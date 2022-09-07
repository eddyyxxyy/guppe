"""
5) Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""
from collections import deque
from locale import atof, format_string


def get_float(msg: str) -> float:
    while True:
        try:
            number = atof(input(msg).strip())
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def main():
    numbers = deque()
    for i in range(10):
        numbers.append(
            get_float(f'Enter {i + 1}º number:\n-> ')
        )
    formatted_numbers = ', '.join(
        format_string('%.1f', num) for num in numbers
    )
    print('\n' + '-' * 30)
    print(
        '\nNumbers:'
        f'\n-> {formatted_numbers}'
        '\nAmount of even numbers:\n->',
        len([number for number in numbers if number % 2 == 0])
    )


if __name__ == '__main__':
    main()

"""
pares = []
n = []
for i in range(10):
    n.append(int(input('Informe um número: ')))
    if n[i] % 2 == 0:
        pares.append(n[i])
print(f'O vetor {n} tem {len(pares)} números pares, a lista de pares é {pares}.')
"""
