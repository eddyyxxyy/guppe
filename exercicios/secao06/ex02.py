"""
2) Escreva um prorgama que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes.
A primeira vez deve usar a estrutura de repetição for, a segunda while.
"""

print(
    '=' * 24 + '\n' +
    'DE 1 A 100, DUAS VEZES'.center(24, '-') + '\n' +
    '=' * 24 + '\n'
)

for i in range(1, 101):
    print(str(f'{i},').ljust(3), end=' ')
    if i % 10 == 0:
        print()

print()

cont: int = 1
while cont <= 100:
    print(str(f'{cont},').center(3), end=' ')
    if cont % 10 == 0:
        print()
    cont += 1