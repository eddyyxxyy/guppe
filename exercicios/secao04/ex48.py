"""
48) Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos
"""
seg = float(input('Informe um valor em segundos: ').strip())
seg = seg % (24 * 3600)
hor = seg // 3600
seg %= 3600
minut = seg // 60
seg %= 60
print(f'Em horas, minutos e segundos: {hor:.0f}:{minut:.0f}:{seg:.0f}')
