"""
49) Faça um programa para ler o horário (hora, minuto e segundo)
de ínicio e duração em segundos, de uma experiência biológica.
O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma.
"""
print('Preencha os campos abaixo com o horário atual:')
hour = int(input('Hora: '))
minute = int(input('Minuto: '))
seg = int(input('Segundo: '))
duracao = int(input('\nDuração do evento (segundos): '))
seg_final = (seg + duracao) % 60
minute_final = (minute + (seg + duracao) // 60) % 60
hour_final = (hour + (minute + (seg + duracao) // 60) // 60) % 24
print(
    f'O fim do evento se dará às '
    + f'{hour_final}h {minute_final}min {seg_final}s.'
)
