"""
19) Faça uma função que retorne o maior fator primo de um número.
"""
from locale import LC_ALL, atoi, setlocale


def get_int(name: str):
    while True:
        try:
            value = atoi(input(f'Enter {name}:\n->'))
            return value
        except ValueError:
            print(f'\033[31mINVALID {name.upper()}! Try again...\033[m\n')


def maior_primo(n):
    for num in reversed(range(1, n + 1)):
        if all(num % i != 0 for i in range(2, num)):
            return num


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    num = get_int('a')
    primo = maior_primo(num)
    print(f'\nLargest prime number before {num:n}' f'\n-> {primo}')


if __name__ == '__main__':
    main()
