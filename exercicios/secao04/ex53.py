"""
53) Faça umm programa para ler as dimensões de um terreno
(comprimento c e largura l), bem como o preço do metro de tela p.
Imprima o custo para cercar este mesmo terreno com tela.
"""
c = float(
    input('Informe o cumprimento do terreno em metros: ')
    .strip()
    .replace(',', '.')
)
l = float(
    input('Informe a largura do terreno em metros: ').strip().replace(',', '.')
)
t = float(
    input('Informe o preço da tela para cercar o terreno: \033[37mR$\033[m')
    .strip()
    .replace(',', '.')
)
print(
    f'O valor pago para cobrir o terro com a tela é de: \033[37mR$\033[m{c * 2 * l * 2 * t:.2f}'
)
