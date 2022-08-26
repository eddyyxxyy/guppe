"""
3) Leia um número real. Se o número for positivo imprima a raiz quadrada.
Do contrário, imprima o número ao quadrado.
"""
from math import sqrt

n = float(input('Informe um número real: ').strip().replace(',', '.'))
if n == 0:
    print('O número 0 é não possui raiz quadrada e, se elevado ao quadrado, também resulta em 0.')
elif n > 0:
    print(f'A raiz quadrada de {n} é {sqrt(n)}')
else:
    print(f'O número {n} elevado ao quadrado resulta em {n ** 2}')
