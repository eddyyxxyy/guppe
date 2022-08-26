"""
52) Três amigos jogaram na loteria. Caso eles ganhem,
o prêmio deve ser repartido porporcionalmente ao valor
que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio,
e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""
vp = float(input('Informe o valor do prêmio: \033[37mR$\033[m').strip().replace(',', '.'))
j1 = float(input('Informe quanto o jogador 1 investiu na aposta: \033[37mR$\033[m').strip().replace(',', '.'))
j2 = float(input('Informe quanto o jogador 2 investiu na aposta: \033[37mR$\033[m').strip().replace(',', '.'))
j3 = float(input('Informe quanto o jogador 3 investiu na aposta: \033[37mR$\033[m').strip().replace(',', '.'))
total = j1 + j2 + j3
print(f'O jogador 1 receberá: \033[37mR$\033[m{(j1 / total) * vp:.2f}')
print(f'O jogador 2 receberá: \033[37mR$\033[m{(j2 / total) * vp:.2f}')
print(f'O jogador 3 receberá: \033[37mR$\033[m{(j3 / total) * vp:.2f}')
