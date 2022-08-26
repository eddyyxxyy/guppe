"""
19) Faça um programa para verificar se um determinado número
inteiro é divisível por 3 ou 5, mas não simultaneamente pelos dois.
"""
print('-=' * 15 + '\n' + 'Verificador de Divisores'.center(30, '-') + '\n' + '=-' * 15)
while True:
    try:
        n: int = int(input('Informe um número inteiro: ').strip())
    except ValueError:
        print(f'Valor inválido!')
        continue
    else:
        if n % 3 == 0 or n % 5 == 0:
            if n % 3 == 0 and n % 5 == 0:
                print(f'O número {n} é divisível por 3 e 5!')
                break
            elif n % 3 == 0 and n % 5 != 0:
                print(f'O número {n} é divisível por 3 e não por 5!')
                break
            elif n % 3 != 0 and n % 5 == 0:
                print(f'O número {n} é divisível por 5 e não por 3!')
                break
        else:
            print(f'O número {n} não é divisível por 3 e nem por 5!')
            break
