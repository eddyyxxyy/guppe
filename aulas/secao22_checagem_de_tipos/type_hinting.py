"""
Dica de tipo - Type Hinting - PEP 484

É uma solução formal para indicar estáticamente
o tipo de um dado em uma linguagem de programação
com tipagem dinâmica, como é o caso do Python.

No Python, o tipo de dado é atribuido de acordo
com o valor. Porém, com Type Hinting, podemos
fazer isso de forma diferente.
"""
# Um exemplo em funções:


def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}!'


print(cumprimentar('Edson'))
