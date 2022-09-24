"""
41) Faça uma função que receba um vetor de inteiros e retorne o maior valor
"""


def get_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def max_array(*args) -> int:
    return max(*args)


def main() -> None:
    array = []
    for i in range(10):
        array.append(
            get_int(f'Enter integer for position {i + 1}: ')
        )
    print(
        '\nArray:'
        f'\n-> {array}'
        '\n\nLargest value in Array:'
        f'\n-> {max_array(array)}'
    )


if __name__ == '__main__':
    main()
