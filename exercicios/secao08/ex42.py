"""
42) Faça uma função que receba um vetor de reais e retorne a média
dele.
"""
from statistics import mean


def max_array(*args) -> int:
    return mean(args)


def main() -> None:
    print(max_array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


if __name__ == '__main__':
    main()
