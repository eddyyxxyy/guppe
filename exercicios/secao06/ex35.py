"""
35) Faça um programa que some os números impares contidos em um intervalo
definido pelo usuário. O usuário define o valor inicial do intervalo
e o valor final deste intervalo e o programa deve somar todos os números
impares contidos. Caso o usuário digite um intervalo inválido (começando por um valor
maior que o valor final) deve ser escrito uma mensagem de erro na tela, "Intervalo de
valores inválido" e o programa termina. Exemplo de tela de saída:
Digte o valor incial e valor final: 5 e 10
Soma dos ímpares neste intervalo: 21
"""
from locale import atoi


def get_integer(msg: str = 'Enter an integer:\n-> ') -> int:
    while True:
        try:
            number = atoi(input(msg).strip())
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def sum_odds_inrange() -> int:
    while True:
        start = get_integer('Enter an integer to start of range:\n-> ')
        end = get_integer('Enter an integer to end of range:\n-> ') + 1
        if start < end:
            break
        else:
            print('Start number must be less than the end number.\n')
    result: int = 0
    for num in range(start, end):
        if num % 2 != 0:
            result += num
    return result


def main():
    print('Sum of odd numbers in range of n to n\n')
    sum_of_odds = sum_odds_inrange()
    print('\nSum:' f'\n-> {sum_of_odds}')


if __name__ == '__main__':
    main()
