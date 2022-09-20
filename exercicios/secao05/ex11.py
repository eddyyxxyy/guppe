"""
11) Escreva um programa que leia um número inteiro maior do que zero
e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número
251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não dor maior do que
zero, programa terminará com a mensagem 'Número inválido'
"""
n = str(
    input('Informe um número inteiro positivo: ').strip().replace(',', '.')
)
try:
    int(n)
except ValueError:
    print(f'O valor informado: {n}\nNão é válido!')
    exit()
else:
    algaris = tuple((int(algaris) for algaris in n))
    print(
        f'Os algarismos do número {n} são: '
        + f'{algaris};\n'
        + f'A soma desses algarimos de {n} é {sum(algaris)}!'
    )
