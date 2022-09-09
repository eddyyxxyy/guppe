"""
20) Escreva um programa que leia números inteiros no intervalo [0,50]
e os armazene em um vetor com 10 posições. Preencha um segundo vetor
apenas com os números ímpares do primeiro vetor. Imprima os dois vetores,
2 elementos por linha.
"""
from collections.abc import Iterator
from locale import setlocale, LC_ALL, atoi


def get_ints_0_to_50(n: int) -> Iterator[int]:
    for i in range(n):
        while True:
            try:
                number = atoi(
                    input(
                        f'Enter the {i + 1}º integer: '
                        '\033[37mIntegers between 0 and 50 (inclusive)\033[m'
                        '\n-> '
                    )
                )
                if number < 0 or number > 50:
                    raise ValueError
                yield number
                break
            except ValueError:
                print('Invalid integer! Try again...\n')


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = tuple(get_ints_0_to_50(10))
    odd_numbers = tuple(x for x in numbers if x % 2 != 0)
    print(f"\nNumbers: ")
    for i in range(0, len(numbers), 2):
        print(f"{numbers[i]}   ", end='')
        if len(numbers) > i + 1:
            print(numbers[i + 1])
    print(f"\nOdd numbers: ")
    for i in range(0, len(odd_numbers), 2):
        print(f"{odd_numbers[i]}   ", end='')
        if len(odd_numbers) > i + 1:
            print(odd_numbers[i + 1])


if __name__ == '__main__':
    main()
