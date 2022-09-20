"""
55) Escreva um programa que leia um inteiro não negativo n e imprima a soma
dos n primeiros números primos.
"""


def get_positive_int(msg: str) -> int:
    while True:
        try:
            number: int = int(input(msg).strip())
            if number < 1:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...')


def prime_numbers(number: int) -> int:
    soma = 0
    conta = 0
    num = 2
    while conta < number:
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
        if primo:
            soma += num
            conta += 1
        num += 1
    return soma


def main() -> None:
    number = get_positive_int('Enter an positive integer:\n-> ')
    print(f'Sum of {number} prime numbers:', prime_numbers(number))


if __name__ == '__main__':
    main()
