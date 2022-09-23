"""
34) Faça uma função não-recursiva que receba um número inteiro positivo impar N e
retorne o fatorial duplo desse número. O fatorial duplo é definido como
o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N.
Assim, o fatorial duplo de 5 é: 5!! = 1 * 3 * 5 = 15
"""


def get_odd_int(prompt: str):
    while True:
        try:
            odd_int = int(input(prompt))
            if odd_int % 2 != 1:
                raise ValueError
            return odd_int
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def double_factorial(odd_int: int):
    result = 1
    for i in range(1, odd_int + 1, 2):
        # print(i, result)
        result = result * i
    return result


def main() -> None:
    odd_int = get_odd_int('Enter odd integer: ')
    result = double_factorial(odd_int)
    print(f'\nResult of {odd_int}!:' f'\n-> {result}')


if __name__ == '__main__':
    main()
