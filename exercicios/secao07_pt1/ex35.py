"""
35) Faça um programa que leia dois números a e b (positivos menores
que 10000) e:
    . Crie um vetor onde cada posição é um algorismo do número. A primeira
    posição é o algarismo menos significativo;
    . Crie um vetor que seja a soma de a e b, mas faça faça-o usando
    apenas os vetores construídos anteriormente.
Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia
10 do resultado e some 1 à próxima posição.
"""
from locale import LC_ALL, atoi, format_string, setlocale


def get_int(name: str) -> int:
    while True:
        try:
            number = atoi(input(f'Enter a number for "{name}":\n-> '))
            if number < 0 or number > 10000:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a = sorted(list(map(int, str(get_int('a')))))
    b = sorted(list(map(int, str(get_int('b')))))
    v = tuple(x + y for x, y in zip(a, b))
    print(
        '\nFirst array:' f'\n->',
        ', '.join(format_string('%d', x) for x in a) + '.'
        '\nSecond array:'
        f'\n->',
        ', '.join(format_string('%d', x) for x in b) + '.'
        '\nSum of arrays:'
        f'\n->',
        ', '.join(format_string('%d', x) for x in v),
        end='.',
    )


if __name__ == '__main__':
    main()
