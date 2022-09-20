"""
60) Faça um programa que leia vários números, calcule e mostre:
(a) A soma dos números digitados
(b) A quantidade de números digitados
(c) A média dos números digitados
(d) O maior número digitado
(e) O menor número digitado
(f) A média dos números pares
Finalize a entrada de dados caso o usuário informe o valor 0.
"""
from collections.abc import Iterator
from locale import LC_ALL, atoi, format_string, setlocale


def get_numbers(msg: str) -> Iterator[int]:
    while True:
        try:
            number = atoi(input(msg).strip())
            if number <= 0:
                return None
            yield number
        except ValueError:
            print('Invalid number! Try again...\n')


def main() -> None:
    setlocale(LC_ALL, 'pt-BR')
    numbers = tuple(
        get_numbers(
            'Enter an integer: \033[37m0 or less to stop\033[m' '\n-> '
        )
    )
    formatted_numbers = ', '.join(
        format_string('%d', x) for x in numbers if len(numbers) >= 1
    )
    print(
        '-' * 30 + '\n' + '\nNumbers:'
        f"\n-> {formatted_numbers if formatted_numbers != '' else '..'}."
        '\na) Sum of all numbers:'
        f'\n-> {sum(numbers)}'
        '\nb) Amount of numbers:'
        f'\n-> {len(numbers)}'
        '\nc) Average of all numbers:'
        f'\n-> {sum(numbers) / len(numbers):n}'
        '\nd) Highest number:'
        f'\n-> {max(numbers)}'
        '\ne) Lowest number:'
        f'\n-> {min(numbers)}'
        '\nf) Average of all even numbers:'
        f'\n-> {sum(nums for nums in numbers if nums % 2 == 0) / len([nums for nums in numbers if nums % 2 == 0]):n}'
    )


if __name__ == '__main__':
    main()
