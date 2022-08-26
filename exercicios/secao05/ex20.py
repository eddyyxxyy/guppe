"""
20) Dados três valores A, B, C, verificar se eles podem ser valores
dos lados de um triângulo e, se forem, se é um triângulo escaleno,
equilátero ou isóscele, considerando os seguintes conceitos:
    - O comprimento de cada lado de um triângulo é menor
do que a soma dos outros dois lados.
    - Chama-se equilátero o triângulo que tem três lados iguais
    - Denominam-se isósceles o triângulo que tem o comprimento
de dois lados iguais.
    - Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""
print('-=' * 15 + '\n' + 'Verificador de Triângulos'.center(30, '-') + '\n' + '=-' * 15)
a, b, c = 0, 0, 0
while True:
    try:
        a = float(input('\nInforme o comprimento do lado A: ').strip().replace(',', '.'))
    except ValueError:
        print('Valor inválido!')
        continue
    else:
        if a <= 0:
            print('Valor inválido!')
            continue
        while True:
            try:
                b = float(input('\nInforme o comprimento do lado B: ').strip().replace(',', '.'))
            except ValueError:
                print('Valor inválido!')
                continue
            else:
                if b <= 0:
                    print('Valor inválido!')
                    continue
                while True:
                    try:
                        c = float(input('\nInforme o comprimento do lado C: ').strip().replace(',', '.'))
                    except ValueError:
                        print('Valor inválido!')
                        continue
                    else:
                        if c <= 0:
                            print('Valor inválido!')
                            continue
                    break
            break
    break
if a > (b + c) or b > (a + c) or c > (a + b):
    print(f'\nCom os comprimentos informados não é possível formar um triângulo.')
else:
    if a == b == c:
        print(f'\nO triângulo formado com os comprimentos {a}, {b} e {c} é equilátero!')
    elif a != b != c != a:
        print(f'\nO triâgulo formado com os comprimentos {a}, {b} e {c} é escaleno!')
    else:
        print(f'\nO triângulo formado com os comprimentos {a}, {b} e {c} é isósceles!')
