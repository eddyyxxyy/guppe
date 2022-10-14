"""
Manipulando Datas e Horas

O Python tem um módulo built-in para se trabalhar com data e hora,
chamado datetime.

Exemplos:

# Introdução

import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2022-10-14 13:20:05.702191

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterando horário para 16 horas, 0 min, 0 sec, 0 microsec
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)
print(inicio)


# Recebendo a data do usuário e convertendo para
# data

import datetime

evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))
print(type('31/12/2018'))
print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/aaaa): ')

nascimento = nascimento.split('/')
nascimento = datetime.datetime(
    int(nascimento[2]),
    int(nascimento[1]),
    int(nascimento[0]),
)

print(type(nascimento))
print(nascimento)



# Acesso individual dos elementos de data e hora

import datetime

evento = datetime.datetime.now()

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

print(dir(evento))
"""
