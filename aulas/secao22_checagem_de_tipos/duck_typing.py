"""
Duck Typing

O Tipo ou a Classe de um objeto, é menos importante
que os métodos que o definem. Ao invés de checar a
Classe ou Tipo de dado, é checada a presença ou não
de métodos ou atributos específicos.
"""


class CisneNegro:
    def __len__(self):
        return 42


livro = CisneNegro()

print(len(livro))

nome = 'Edson Pimenta'
lista = [12, 34, 55, 49]
dicio = {'Carlos': 12, 'Vanessa': 34, 'Joana': 49}

print(len(nome))
print(len(lista))
print(len(dicio))
