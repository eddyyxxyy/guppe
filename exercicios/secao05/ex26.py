"""
26) Leia a distância em km e a quantidade de litros de gasolina consumidos
por um carro em um percurso, calcule o consumo em km/l e escreva uma mensagem
de acordo com a tabela abaixo:
    CONSUMO     |  (Km/l)  |   MENSAGEM
    menor que   |     8    |  Venda o carro!
    entre       |  8 e 12  |     Econômico!
    maior que   |    12    |  Super econômico!
"""
print('-=' * 15 + '\n' + 'QUILÔMETRO POR LITROS'.center(30, '-') + '\n' + '-=' * 15)
dkm: float = 0
litro: float = 0
km_por_l: float = 0
while True:
    try:
        dkm = float(input('Informe a distância em quilômetros percorridos: ').strip().replace(',', '.'))
    except ValueError:
        print('Valor inválido!')
        continue
    else:
        if dkm <= 0:
            print('O valor precisa ser maior que 0!')
            continue
        while True:
            try:
                litro = float(input('Informe quantos litros foram gastos: ').strip().replace(',', '.'))
            except ValueError:
                print('Valor inválido!')
                continue
            else:
                if litro <= 0:
                    print('O valor precisa ser maior que 0!')
                    continue
                else:
                    km_por_l = dkm / litro
                    break
        break
print(f'{km_por_l:.1f}km/l')
if km_por_l < 8:
    print('Venda o carro!')
elif 8 <= km_por_l <= 12:
    print('Econômico!')
else:
    print('Super econômico!')
