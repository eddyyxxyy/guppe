"""
37) As tarifas de certo parque de estacionamento são as seguintes:
    - 1ª e 2ª hora - R$1,00 cada
    - 3ª e 4ª hora - R$1,40 cada
    - 5ª hora e seguintes - R$2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por execesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida deste
sao apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12,50 representará 'dez para a uma da tarte'. Pretende-se
criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva
na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida
se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada
for superior à da partida, isso não é uma situação de erro, antes significará que
a partida ocorreu no dia seguinte ao chegada.
"""
from ex36_functions import real_br_money_mask

hora_chegada: int
hora_partida: int
min_chegada: int
min_partida: int
hora_final: int
min_final: int
min_total: int


print(
    '=' * 44 + '\n' + 'ESTACIONAMENTO'.center(44, '-') + '\n' + '=' * 44 + '\n'
)
while True:
    try:
        hora_chegada, min_chegada = [
            int(x)
            for x in input(
                'Digite a hora e minuto de chegada: \033[37mEx: 12 50\033[m\n'
                '->  '
            ).split()
        ]
    except ValueError:
        print('\nValor inválido! Tente novamente...\n')
    else:
        while True:
            try:
                hora_partida, min_partida = [
                    int(x)
                    for x in input(
                        'Digite a hora e minuto de saída: \033[37mEx: 14 30\033[m\n'
                        '->  '
                    ).split()
                ]
            except ValueError:
                print('\nValor inválido! Tente novamente...\n')
            else:
                break
        break

if hora_chegada > hora_partida:
    hora_partida = hora_partida + 24
if min_chegada > min_partida:
    min_partida = min_partida + 60
    hora_partida = hora_partida - 1

min_final = min_partida - min_chegada
hora_final = hora_partida - hora_chegada

if hora_final >= 1:
    if min_final > 1:
        print(
            f'O carro ficou estacionado durante {hora_final} horas e {min_final} minutos.'
        )
    else:
        print(f'O carro ficou estacionado durante {hora_final} horas.')
else:
    print(f'O carro ficou estacionado durante {min_final} minutos.')

min_total = int((hora_final * 60) + min_final)

if min_total <= 120:
    if min_total <= 60:
        preco = 1.00
        print(f'Preço total: R${real_br_money_mask(preco)}.')
    else:
        preco = 2
        print(f'Preço total: R${real_br_money_mask(preco)}.')
elif min_total <= 240:
    if min_total <= 180:
        preco = 2 + 1.40
        print(f'Preço total: R${real_br_money_mask(preco)}')
    else:
        preco = 2 + (1.40 * 2)
        print(f'Preço total: R${real_br_money_mask(preco)}')
else:
    hora_total = int(min_total // 60)
    preco = 4.40 + ((hora_total - 4) * 2)
    print(f'Preço total: R${real_br_money_mask(preco)}')
