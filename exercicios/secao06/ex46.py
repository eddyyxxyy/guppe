"""
46) Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar
acertar qual o número foi gerado, a cada tentativa o programa deverá informar se o
chute é menor ou maior que o número gerado. O programa acaba quando o usuário acerta
o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.
"""
from locale import atoi
from random import randint


def get_number(msg: str = 'Enter a number:\n-> ') -> int:
    while True:
        try:
            number = atoi(input(msg).strip())
            if number <= 0 or number > 1000:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def another_game() -> str:
    while True:
        try:
            another_one = str(input('\n\033[90mPC\033[m: Want to try again?\n-> ').strip().lower()[0])
            if another_one not in 'yn':
                raise KeyError
            return another_one
        except ValueError:
            print('Invalid choice! Try again...')


def main() -> None:
    while True:
        pc_number = randint(1, 1000)
        while True:
            print(
                f"\033[90mPC\033[m: "
                f"I'm thinking in a number, between 1 and 1000. Try to guess..."
                f"\n-> ", end=''
            )
            player_number = get_number('')
            if player_number != pc_number:
                if pc_number < player_number:
                    print('Less than that...\n')
                else:
                    print('More than that...\n')
            else:
                print(
                    '\033[90mPC\033[m: YOU DID IT! YOU ARE ABOSOLUTELY RIGHT MY FELLOW HUMAN!'
                    f'\n\033[90mPC\033[m: I was thinking of {pc_number}! Haha!'
                )
                break
        keep_playing = another_game()
        if keep_playing == 'y':
            print('\n\033[90mPC\033[m: Well, lets go!\n')
        else:
            print('\n\033[90mPC\033[m: Bye bye, so long!')
            break


if __name__ == '__main__':
    main()
