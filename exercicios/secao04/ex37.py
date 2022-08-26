"""
37) Faça um programa que leia o valor de um produto e imprima
o valor com desconto, tendo em vista que o desconto foi de 12%.
"""
n = float(str(input('Informe o valor do produto: \033[37mR$\033[m').strip().replace(',', '.')))
print(f'Com o desconto de 12%, o valor do produto é de R${n * 0.88:.2f}.')
