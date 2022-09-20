"""
2) Crie um programa que lê 6 valores inteiros e, em seguida,
mostre na tela os valores lidos
"""
from collections import deque


def get_number(msg: str) -> int:
    while True:
        try:
            number = int(input(msg).strip())
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def main() -> None:
    values = deque()
    for i in range(6):
        values.append(get_number(f'Enter {i + 1}º integer:\n-> '))
    print('\nValues:\n-> ', end='')
    print(*values, sep=',', end='.')


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:

numeros: list = []
for numero in range(6):
    numeros.append(int(input('Informe um número inteiro: ')))
print(numeros)
"""
