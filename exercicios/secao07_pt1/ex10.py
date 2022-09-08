"""
10) Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor,
calcule e imprima a média geral.
"""
from collections.abc import Iterator
from locale import atof, setlocale, LC_ALL


def get_floats(n: int) -> Iterator[float]:
    count: int = 1
    for i in range(n):
        while True:
            try:
                number = atof(
                    input(f'Enter the {count}º grade:\n-> ')
                )
                if number < 0 or number > 10:
                    raise ValueError
                yield number
                break
            except ValueError:
                print('Invalid grade value! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = tuple(get_floats(15))
    print(
        '-' * 30 +
        f'\nAverage from grades: {sum(numbers) / len(numbers)}'
    )


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:

nota_alunos = []
for i in range(15):
    nota_alunos.append(float(input(f'Informe a nota do {i + 1}º aluno: ')))
print(f'A média geral da sala foi de {sum(nota_alunos) / len(nota_alunos):.1f}')
"""