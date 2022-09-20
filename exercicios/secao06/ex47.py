"""
47) Faça um programa que apresente um menu de opções para o cálculo
das seguintes operações entre dois números:
    - adição (opção 1)
    - subtração (opção 2)
    - multiplicação (opção 3)
    - divisão (opção 4)
    - saídaa (opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejaada,
a exibição do resultado e a volta ao menu de opções. O programa só termina
quando for escolhida a opção de saída (opção 5).
"""
from locale import atof, atoi
from time import sleep


def title_menu(msg: str = 'MATH OPERATIONS MENU') -> str:
    string_title = str(
        '=' * 22 + '\n' + msg.center(22, '-') + '\n' + '=' * 22 + '\n'
        '1 - Sum;'
        '\n2 - Subtraction;'
        '\n3 - Multiplication;'
        '\n4 - Division;'
        '\n5 - Exit.'
    )
    return string_title


def get_choice_menu(msg: str = '-> ') -> int:
    while True:
        try:
            choice = atoi(input(msg).strip())
            if choice < 1 or choice > 5:
                raise ValueError
            return choice
        except ValueError:
            print('Invalid choice! Try again...')


def get_numbers_operation() -> tuple[float, float]:
    while True:
        try:
            n1 = atof(input('Enter the first number:\n-> ').strip())
            n2 = atof(input('Enter the second number:\n-> ').strip())
            return n1, n2
        except ValueError:
            print('Invalid number! Try again...')


def operations(choice: int, numbers: tuple) -> float:
    if choice == 1:
        return sum(numbers)
    elif choice == 2:
        return numbers[0] - numbers[1]
    elif choice == 3:
        return numbers[0] * numbers[1]
    elif choice == 4:
        return numbers[0] / numbers[1]
    else:
        return 5


def main() -> None:
    menu = title_menu()
    while True:
        print(menu)
        choice = get_choice_menu()
        if choice == 5:
            print('Shutting down...')
            sleep(2)
            break
        numbers = get_numbers_operation()
        result = operations(choice, numbers)
        print('\nResult:' + f'\n-> {result}\n' + '-' * 22)
        sleep(2)


if __name__ == '__main__':
    main()
