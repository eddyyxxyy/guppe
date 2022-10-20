"""
Tipos em Comentários


import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(8))
print(circunferencia.__annotations__)  # retorna dict vázio


def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return texto
    return 'a'


# cabecalho1(43, 'Edson')

def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
): # type: (...) -> str
    if alinhamento:
        return texto
    return 'a'


cabecalho2(43, 'Edson')

nome = 'Edson'  # type: str
"""
