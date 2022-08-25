vt = float(input('Informe o valor total à ser pago: \033[37mR$\033[m').strip().replace(',', '.'))
print(f'Pagar com 10% de desconto: R${vt * 0.90:.2f};\n'
      f'Parcelado 3 vezes: R${vt / 3:.2f};\n'
      f'Comissão do vendedor se pago à vista (5% sobre o valor com desconto): R${(vt * 0.90) * 0.05};\n'
      f'Comissão do vendedor se pago parcelado em 3x (5% sobre valor total): R${vt * 0.05}.')
