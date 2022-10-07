"""
POO - MRO: Method Resolution Order

Method Resolution Order - Resolução de Ordem de Métodos - é a ordem de
execução dos métodos. Ou seja, quem será executado 'primeiro'.

Em Python, podemos conferir a ordem de execução dos métodos de 3 formas:
    - Via propriedade da Classe: NomeCLasse.__mro__
    - Via método: NomeCLasse.method()
    - Via help: help(NomeCLasse)

Se invertermos a ordem das Heranças na declaração da Classe Pinguim, o método
da Super Classe que estiver declarada primeiro é o que prevalecerá.
"""
from heranca_multipla import Pinguim

# Testando

pinguim = Pinguim('Tux')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimenta())
