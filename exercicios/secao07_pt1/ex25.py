"""
25) Faça um programa que preencha um vetor de tamanho 100
com os 100 primeiros naturais que não são múltiplos de 7 ou
que terminam com 7.
"""
from locale import LC_ALL, setlocale


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = []
    while len(numbers) < 100:
        numbers = [x for x in range(130) if x % 7 != 0 and x % 10 != 7]
    print('Numbers:' f'\n-> {numbers}')


if __name__ == '__main__':
    main()
