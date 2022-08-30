"""
3) Faça um algoritmo utilizando o comando while que mostra uma mensagem
regressiva na tela, inciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!"
após a contagem
"""

print(
    '=' * 21 + '\n' +
    'DE 10 A 0 (WHILE)'.center(21, '-') + '\n' +
    '=' * 21 + '\n'
)

cont: int = 10
while cont != -1:
    print(cont, end=', ')
    cont -= 1
print('FIM!')