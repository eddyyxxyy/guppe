"""
Métodos de Data e Hora

# Exemplos

# Onde podemos usar timezone (fusos)

import datetime

# Com o now() podemos especificar o fuso horário (timezone)
agora = datetime.datetime.now()  # now == agora
print(agora)
print(type(agora))
print(repr(agora))

print()

# Já com o today() não temos fuso horário (timezone)
hoje = datetime.datetime.today()  # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))



# Mudanças ocorrendo à meia noite -> combine()

import datetime

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))



# Encontrar dia da semana, weekday()

import datetime

# Os dias da semana no método weekday() começam no 0, sendo 0
# segunda-feira

# 0 - Segunda-Feira - Monday
# 1 - Terça-Feira - Tuesday
# 2 - Quarta-Feira - Wednesday
# 3 - Quinta-Feira - Thursday
# 4 - Sexta-Feira - Friday
# 5 - Sábado - Saturday
# 6 - Domingo - Sunday

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(manutencao.weekday())  # 1 - Terça-Feira - Tuesday


# Trabalhando com strftime

# %a  -  Abbreviated weekday name.	Sun, Mon, ...
# %A  -  Full weekday name.	Sunday, Monday, ...
# %w  -  Weekday as a decimal number.	0, 1, ..., 6
# %d  -  Day of the month as a zero-padded decimal.	01, 02, ..., 31
# %-d -  Day of the month as a decimal number.	1, 2, ..., 30
# %b  -  Abbreviated month name.	Jan, Feb, ..., Dec
# %B  -  Full month name.	January, February, ...
# %m  -  Month as a zero-padded decimal number.	01, 02, ..., 12
# %-m -  Month as a decimal number.	1, 2, ..., 12
# %y  -  Year without century as a zero-padded decimal number.	00, 01, ..., 99
# %-y -  Year without century as a decimal number.	0, 1, ..., 99
# %Y  -  Year with century as a decimal number.	2013, 2019 etc.
# %H  -  Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
# %-H -  Hour (24-hour clock) as a decimal number.	0, 1, ..., 23
# %I  -  Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
# %-I -  Hour (12-hour clock) as a decimal number.	1, 2, ... 12
# %p  -  Locale’s AM or PM.	AM, PM
# %M  -  Minute as a zero-padded decimal number.	00, 01, ..., 59
# %-M -  Minute as a decimal number.	0, 1, ..., 59
# %S  -  Second as a zero-padded decimal number.	00, 01, ..., 59
# %-S -  Second as a decimal number.	0, 1, ..., 59
# %f  -  Microsecond as a decimal number, zero-padded on the left.	000000 - 999999
# %z  -  UTC offset in the form +HHMM or -HHMM.
# %Z  -  Time zone name.
# %j  -  Day of the year as a zero-padded decimal number.	001, 002, ..., 366
# %-j -  Day of the year as a decimal number.	1, 2, ..., 366
# %U  -  Week number of the year (Sunday as the first day of the week). All days in a new year preceding the
first Sunday are considered to be in week 0.	00, 01, ..., 53
# %W  -  Week number of the year (Monday as the first day of the week). All days in a new year preceding the
first Monday are considered to be in week 0.	00, 01, ..., 53
# %c  -  Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
# %x  -  Locale’s appropriate date representation.	09/30/13
# %X  -  Locale’s appropriate time representation.	07:06:05
# %%  -  A literal '%' character.	%

from locale import LC_ALL, setlocale
import datetime

setlocale(LC_ALL, 'pt_BR.UTF-8')

aniversario = input('Qual sua data de nascimento (dd/mm/aaaa)? ')

aniversario = aniversario.split('/')
aniversario = datetime.datetime(
    year=int(aniversario[2]),
    month=int(aniversario[1]),
    day=int(aniversario[0])
)

print(f"Você nasceu em um(a) {aniversario.strftime('%A')}")



# Uso do locale e formatações

import datetime
# from textblob import TextBlob
from locale import LC_ALL, setlocale


# def formata_data(data: datetime.datetime) -> str:
#     return f'{data.day} de {TextBlob(data.strftime("%B")).translate(to="pt-br")} de {data.year}'
def formata_data(data: datetime.datetime) -> str:
    return f'{data.day} de {data.strftime("%B").capitalize()} de {data.year}'


setlocale(LC_ALL, 'pt_BR.UTF-8')
hoje = datetime.datetime.now()
print(formata_data(hoje))



# Uso do strptime para converter strings em datetime objects

from datetime import datetime

nascimento = datetime.strptime('22/04/2000', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual sua data de nascimento (dd/mm/aaaa)? ')
nascimento = datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)



# Trabalhando somente com horas


import datetime

# Somente hora
almoco = datetime.time(12, 30, 0)

print(almoco)
print(type(almoco))
print(repr(almoco))



# Marcando tempo de execução do nosso código com timeit

import timeit

# Loop for
tempo = timeit.timeit('".".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('".".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('".".join(map(str, range(100)))', number=10000)
print(tempo)
"""
import functools
import timeit


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma += num**num + 4
    return soma


print(timeit.timeit((functools.partial(teste, 2)), number=10000))
