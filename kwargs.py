"""
Entendendo **kwargs:

- Por convensão o chamamos assim, **kwargs, porém pode ser chamado de qualquer coisa;
- Este é somente mais um parâmetro, mas diferente do *args que coloca os elementos em uma tupla, o **kwargs exige que
utilizemos parâmetros nomeados e transforma esses parâmetros extras em dicionários;


# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs;


Exemplo:


def cores_favoritas(**kwargs):
    print(kwargs)
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor};')


cores_favoritas(marcos='Verde', julia='Amarelo', fernanda='Azul', vanessa='Branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios;

Outro exemplo de uso:


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é...'


print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Java'))
print(cumprimento_especial(lump='Kera'))


Exemplo:


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome}, tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


# Por que é importante manter essa ordem?
- Pois com a declaração na ordem correta não teremos problemas com a atribuição decada valor.

# Para desempacotar o **kwargs só precisamos do "**" em vez de "*", como era feito no *args.
"""
