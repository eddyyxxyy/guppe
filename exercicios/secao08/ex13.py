"""
13) Faça uma função que receba dois valores numéricos e um símbolo.
Este símbolo representará a operação que se deseja efetuar com os
números. Se o símbolo for + deverá ser realizada uma adição, se for -
uma subtração, se for / uma divisão e se for * será efetuada uma multiplicação.
"""
from locale import LC_ALL, atof, setlocale


def calc(a, b, symbol='+') -> float:
    if symbol == '+':
        return a + b
    elif symbol == '-':
        return a - b
    elif symbol == '/':
        return a / b
    else:
        return a * b


def get_number(name: str) -> float:
    while True:
        try:
            value = atof(input(f'Enter no. for "{name}":\n-> '))
            return value
        except ValueError:
            print('\033[31mINVALID! Try again...\033[m\n')


def get_op() -> str:
    while True:
        op = input(
            'Choose the operation to be performed:'
            '\n+ -> Sum'
            '\n- -> Sub'
            '\n/ -> Div'
            '\n* -> Mul'
            '\n-> '
        ).strip()[0]
        if op not in {'+', '-', '/', '*'}:
            print('\033[31mINVALID! Try again...\033[m\n')
            continue
        return op


def main() -> None:
    setlocale(LC_ALL, '')
    a = get_number('A')
    b = get_number('B')
    op = get_op()
    result = calc(a, b, op)
    print('\nOperation:' f'\n{a:n} {op} {b:n} = {result:n}')


if __name__ == '__main__':
    main()
