n = float(str(input('Informe o valor do produto: \033[37mR$\033[m').strip().replace(',', '.')))
print(f'Com o desconto de 12%, o valor do produto é de R${n * 0.88:.2f}.')
