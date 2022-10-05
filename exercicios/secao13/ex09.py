"""
9) Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo
com o conteúdo dos dois primeiros (o conteúdo do primeiro seguido do conteúdo do
segundo).
"""


def join_text(path0: str, path1: str, new_arq: str):
    with open(path0, 'r') as arq0, open(path1, 'r') as arq1, open(
        new_arq, 'w'
    ) as new_arq:
        new_arq.write(arq0.read() + '\n' + arq1.read())


def main() -> None:
    join_text(
        'arquivos/ex09_arq0.txt',
        'arquivos/ex09_arq1.txt',
        'arquivos/ex09_new_arq.txt',
    )
    with open('arquivos/ex09_new_arq.txt') as f:
        print(f.read())


if __name__ == '__main__':
    main()
