"""
30) Leia um valor em real e a cotação do dólar. Em sequida,
imprima o valor correspondente em dólares
"""
# Dolar = 5,17 / Real
vr = float(input('Informe o valor em reais: \033[37mR$\033[m ').strip().replace(',', '.'))
print(f'O valor de R${vr:.2f} em doláres ${vr / 5.17:.2f}.')
