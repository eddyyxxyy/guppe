"""
32) Leia um número inteiro e imprima a soma do sucessor
de seu triplo com o antecessor e seu dobro.
"""
n = int(
    input(
        'Informe um número para saber a soma do sucessor de seu triplo com o dobro de seu antecessor: '
    )
)
print(f'A soma é: {((n * 3) + 1) + ((n - 1) * 2)}')
