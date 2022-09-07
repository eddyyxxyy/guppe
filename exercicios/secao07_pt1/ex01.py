"""
1) Faça um programa que possua um vetor denominado A que armazene 6 números
inteiros. O programa deve executar os seguintes passos:
(A) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(B) Armazene em uma variável inteira(simples) a soma entre os valores das posições
A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
(C) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(D) Mostre na tela cada valor do vetor A, um em cada linha.
"""


def main() -> None:
    # A:
    a = [1, 0, 5, -2, -5, 7]
    # B:
    int_var = sum((a[0], a[1], a[5]))
    # C:
    a[4] = 100
    # D:
    for element in a:
        print(element)


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:

a = [1, 0, 5, -2, -5, 7]
soma = a[0] + a[1] + a[5]
print(f'O valor da soma dos valores na posição 0, 1 e 5 é: {soma}')
a[4] = 100
for indice, numero in enumerate(a):
    print(f'O valor na posição {indice}: {numero}')
"""
