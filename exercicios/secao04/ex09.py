# K = C + 273.15
tc = str(input('Informe a temperatura em ºC: ')).strip().replace(',', '.')
print(f'A temperatuda {float(tc):.2f}ºC em ºK corresponde a: {float(tc) + 273.15:.2f}')
