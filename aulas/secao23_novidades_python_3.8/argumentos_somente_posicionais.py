"""
Argumentos somente posicionais

São argumentos de métodos e funções que não
podem ser informados com o nome do parâmetro.

Por exemplo:

valor = '62.7'
print(float(x=valor))

Isso gera erro, pois o argumento é somente
posicional. Podemos somente informar o valor.
Desta forma:

print(float(valor))

Usamos isso quando queremos que nossa
função seja executada de forma limpa.

Tudo antes da barrinha será somente posicional.

Primeiro exemplo:

def cumprimenta_v1(nome):
    return f'Olá, {nome}!'


print(cumprimenta_v1('Edson'))
print(cumprimenta_v1(nome='Edson'))


def cumprimenta_v2(nome, /):
    return f'Olá, {nome}!'


print(cumprimenta_v2('Edson'))
print(cumprimenta_v2(nome='Edson'))


E se quisermos mais de um argumento?


def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'{mensagem}, {nome}!'


print(cumprimenta_v3('Edson'))
print(cumprimenta_v3('Edson', mensagem='Hello'))
print(cumprimenta_v3('Edson', 'Bem vindo'))


Mais um exemplo:


def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem}, {nome}!'


print(cumprimenta_v4('Edson'))
print(cumprimenta_v4('Edson', 'Hello'))
print(cumprimenta_v4('Edson', 'Bem vindo'))


Também podemos obrigar à utilizar o parâmetro:


def cumprimenta_v5(*, nome):
    return f'Olá, {nome}!'


print(cumprimenta_v5(nome='Edson'))


Dessa forma, todos os argumentos após o * devem
ter o parâmetro informado.


Agora, juntando tudo isso:


def cumprimentar_v6(nome, /, mensagem='Olá', *, mensagem2):
    return f'{mensagem}, {nome}{mensagem2}'


print(cumprimentar_v6('Edson', mensagem='Hello', mensagem2='!'))
print(cumprimentar_v6('Edson', mensagem2=' tenha um bom dia!'))
"""
