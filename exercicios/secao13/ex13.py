"""
13) Faça um programa que permita que o usuário entre com diversos nomes e telefone
para cadastro, e crie um arquivo com essas informações, uma por linha. O usuário
finaliza a entrada com '0' para o telefone.
"""


def get_name():
    while True:
        try:
            name = str(input('Enter name: '))
            if not name.replace(' ', '').isalpha():
                raise Exception
            return name
        except Exception:
            print('Invalid name! Try again...')


def get_phone():
    while True:
        try:
            phone = str(input('Enter phone number: '))
            if not phone.isnumeric():
                raise Exception
            return phone
        except Exception:
            print('Invalid phone number! Try again...')


def main() -> None:
    with open('arquivos/ex13_arq.txt', 'w') as file:
        while True:
            name = get_name()
            phone = get_phone()
            if phone == '0':
                break
            file.write(name.ljust(60))
            file.write(phone.rjust(19) + '\n')


if __name__ == '__main__':
    main()
