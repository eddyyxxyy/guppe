"""
23) Escreva um programa que leia a profissão e o tempo de serviço (em anos)
de cada um dos 5 funcionários de uma empresa e armazene-os no arquivo "emp.txt".
Cada linha do arquivo corresponde aos dados de um funcionário.
"""


def get_name(prompt: str) -> str:
    while True:
        try:
            name = str(input(prompt))
            if not name.replace(' ', '').isalpha():
                raise Exception
            return name.title()
        except Exception:
            print('Invalid name! Try again...\n')


def get_worked_time(prompt: str) -> int:
    while True:
        try:
            worked_time = int(input(prompt))
            if worked_time < 0:
                raise ValueError
            return worked_time
        except ValueError:
            print('Invalid! Try again...\n')


def main() -> None:
    with open('arquivos/ex23_emp.txt', 'a') as f:
        for employee in range(5):
            f.write(
                get_name(f'Enter {employee + 1}º employee profession: ').ljust(
                    40
                )
                + str(
                    get_worked_time(
                        f'Enter {employee + 1}º employee worked time (in years): '
                    )
                )
                + '\n'
            )


if __name__ == '__main__':
    main()
