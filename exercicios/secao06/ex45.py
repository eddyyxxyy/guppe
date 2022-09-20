"""
45) Faça um algoritmo que converta uma velocidade expressa em km/h
para m/s e vice versa. Você deve criar um menu com as duas opções de
conversão e com uma opção para finalizar o programa. O usuário poderá
fazer quantas conversões desejar, sendo que o programa só será finalizado quando
a opção de finalizar for escolhida.
"""
from locale import atof, atoi
from time import sleep


def get_speed(msg: str = 'Enter speed:\n-> '):
    while True:
        try:
            speed = atof(input(msg).strip())
            if speed <= 0:
                return 0
            return speed
        except ValueError:
            print('Invalid speed! Try again...\n')


def converter(km: str = '\nKm/h to M/s:', m: str = '\nM/s to Km/h:') -> float:
    choice = menu_choice()
    if choice == 1:
        print(km)
        m_s = get_speed() / 3.6
        return m_s
    elif choice == 2:
        print(m)
        km_h = get_speed() * 3.6
        return km_h
    else:
        return exit()


def menu_choice(msg: str = 'Enter a number:\n-> ') -> int:
    while True:
        try:
            choice: int = atoi(input(msg).strip())
            if choice <= 0 or choice >= 4:
                raise ValueError
            return choice
        except ValueError:
            print('Invalid choice! Try again...\n')


def title_menu(msg: str = 'SPEED CONVERTER') -> str:
    string_title = (
        '=' * 30 + '\n' + msg.center(30, '-') + '\n' + '=' * 30 + '\n'
        '1 - Km/h to M/s;'
        '\n2 - M/s to Km/s;'
        '\n3 - Shutdown.'
    )
    return string_title


def main():
    while True:
        print(title_menu())
        choice = converter()
        print('Speed converted:' f'\n-> {choice}')
        sleep(2)


if __name__ == '__main__':
    main()
