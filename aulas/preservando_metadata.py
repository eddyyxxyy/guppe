"""
Preservando Metadatas com Wraps

Metadata/Metadados: Sâo dados intrínsecos em arquivo.
Wraps: São funções que envolvem elementos com diversas finalidades.


# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        '''Eu sou uma função (logar) dentro de outra'''
        print(f'Você está chamdando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    '''Soma dois números.'''
    return a + b


# print(soma(10, 30))

print(soma.__name__)  # logar
print(soma.__doc__)  # 'Eu sou uma função (logar) dentro de outra.'

# ESTÁ RETORNANDO A DOCUMENTAÇÃO DO DECORADOR E NÃO DA FUNÇÃO SOMA


"""

# Resolução do problema

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)  # Fazer o Wrap já resolve o problema, pois "amarra" a documentação somente à função em que está
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamdando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


# print(soma(10, 30))

print(soma.__name__)  # soma
print(soma.__doc__)  # 'Soma dois números.'

print(help(soma))

# DESSA VEZ TEMOS O RETORNO CORRETO!
