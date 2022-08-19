# K = M * 3.6
vms = str(input('Informe a velocidade em m/s: ')).strip().replace(',', '.')
print(f'A velocidade {float(vms):.1f} corresponde a: {float(vms) * 3.6:.1f}km/h')
