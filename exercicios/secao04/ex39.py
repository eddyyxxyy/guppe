"""
39) A importância de R$ 780.000,00 será dividida entre três
ganhadores de um concurso. Sendo que da quantia total:
- O primeiro ganhador receberá 46%;
- O segundo receberá 32%;
- O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores
"""
print(
    'Do prêmio de R$780000,00:\n'
    f'1º Lugar - R${780_000 * 0.46:.2f};\n'
    f'2º Lugar - R${780_000 * 0.32:.2f};\n'
    f'3º Lugar - R${780_000 * 0.22:.2f}.'.replace('.', ',')
)
