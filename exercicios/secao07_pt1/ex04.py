"""
4) Faça um programa que leia um vetor de 8 posições e, em seguida,
leia também dois valores X e Y quaisquer correspondentes a duas posições
no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectivas posições X e Y.
"""
from collections import deque
from locale import LC_ALL, atof, atoi, format_string, setlocale


def get_index_for_sum(limit, x: str = 'x') -> int:
    num = get_int(f'Enter position of {x}:\n-> ', lim=limit)
    return num


def get_int(msg: str, lim: int = 0) -> int:
    if lim == 0:
        while True:
            try:
                number = atoi(input(msg).strip())
                return number
            except ValueError:
                print('Invalid number! Try again...\n')
    else:
        while True:
            try:
                number = atoi(input(msg).strip())
                if number > (lim - 1) or number < 0:
                    raise ValueError
                return number
            except ValueError:
                print('Invalid number! Try again...\n')


def get_float(msg: str) -> float:
    while True:
        try:
            number = atof(input(msg).strip())
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def main() -> None:
    setlocale(LC_ALL, 'en')
    numbers = deque()
    how_many_numbers = get_int('How many numbers you want to enter?\n-> ')
    for i in range(how_many_numbers):
        numbers.append(get_float(f'Enter the {i + 1}º value:\n-> '))
    formatted_numbers = ', '.join(format_string('%.1f', x) for x in numbers)
    print('-' * 30)
    x: int = get_index_for_sum(limit=len(numbers))
    y: int = get_index_for_sum(limit=len(numbers), x='y')
    print('-' * 30)
    print(
        'Numbers:'
        f'\n-> {formatted_numbers}.'
        f'\nSum of x (position {x}) and y (position {y}):'
        f'\n-> {numbers[x]} + {numbers[y]} = {numbers[x] + numbers[y]}'
    )


if __name__ == '__main__':
    main()

"""
lista = []
for i in range(8):
    lista.append(int(input(f'Informe um valor para a posição {i} do vetor: ')))
x = int(input('Informe a posição no vetor que deseja: '))
y = int(input('Informe outra posição no vetor que deseja: '))
print(f'A soma dos valores na posição {x} e {y} são: {lista[x] + lista[y]}')
"""
