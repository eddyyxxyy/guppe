"""
34) Faça um programa para ler 10 números DIFERENTES a serem armazenados
em um vetor. Os dados deverão ser armazenados no vetor na ordem que
forem sendo lidos, sendo que o caso o usuário digite um número
que já foi digitado anteriormente, o programa deverá pedir para ele
digitar outro número. Note que cada valor digitado pelo usuário deve
ser pesquisado no vetor, verificando se ele existe entre os números que
já foram fornecidos. Exibir na tela o vetor final que foi digitado.
"""
from collections import deque
from collections.abc import Iterator
from locale import setlocale, LC_ALL, atof, format_string


def get_non_repeated_numbers(n: int) -> Iterator[float]:
    """
    Yields n float values to return Iterator
    :param n: int
    :return: Iterator[float]
    """
    numbers = deque()
    for i in range(n):
        while True:
            try:
                number = atof(
                    input(f'Enter the {i + 1}º number:\n-> ')
                )
                if number not in numbers:
                    numbers.append(number)
                    yield number
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Invalid number! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    v = tuple(get_non_repeated_numbers(10))
    print(
        '\nArray V values:'
        '\n->', ', '.join(
            format_string("%.1f", x) for x in v
        ), end= '.'
    )


if __name__ == '__main__':
    main()
