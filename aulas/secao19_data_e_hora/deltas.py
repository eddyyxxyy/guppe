"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/aaaa 12:55:34.9939329
data_final   = dd/mm/aaaa 13:34:23.0948484
delta = data_final - data_inicial

# Exemplo

import datetime

# Data de hoje
data_hoje = datetime.datetime.now()

# Data do próximo aniversário
aniversario = datetime.datetime(2023, 4, 22, 0)

# Tempo que falta da data de hoje até o próximo aniversário
tempo_para_aniversario = aniversario - data_hoje  # delta - diferença

print(type(tempo_para_aniversario))
print(repr(tempo_para_aniversario))
print(tempo_para_aniversario)
print(f'Faltam {tempo_para_aniversario.days} dias para o aniversário e...')
print(f'{tempo_para_aniversario.seconds // 60 // 60} horas para o aniversário!')
"""
import datetime

data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)
