"""
18) Faça uma função que receba por parâmero dois valores X e Z.
Calcule e retorne o resultado de X elevado a Z para o programa principal.
Atenção não utilize nenhuma função pronta de exponenciação.
"""
from locale import LC_ALL, setlocale

from exercicios.secao08.ex09 import get_float


def calc(x, z):
    return x**z


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    x = get_float('X')
    z = get_float('Z')
    result = calc(x, z)
    print(
        '\nValues:'
        f'\n-> x: {x:n} | z: {z:n}'
        '\nResult:'
        f'\n-> {x:n}^{z:n} = {result:n}'
    )


if __name__ == '__main__':
    main()
