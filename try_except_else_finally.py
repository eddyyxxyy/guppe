"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DO USUÁRIO DEVE SER TRATADA!

OBS: a função do usuário é DESTRUIR seu sistema.


# Else: é executado somente se não ocorrer a exceção/erro.
# Para cada except podemos ter um else.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou: {num}')



"""
