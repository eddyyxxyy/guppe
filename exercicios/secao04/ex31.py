"""
31) Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
"""
n = int(
    round(
        float(
            input(
                'Informe um número inteiro para saber seu antecessor '
                'e seu sucessor: '
            )
            .strip()
            .replace(',', '.')
        )
    )
)
print(f'O sucessor de {n} é {n + 1};\nE seu antecessor é {n - 1}.')
