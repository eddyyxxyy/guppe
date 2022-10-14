"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços
oferecidos por empresas.


import json

ret = json.dumps(
    ['produtos', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}]
)

print(type(ret))

print(ret)


import json


class Gato:

    def __init__(self, nome, raca):
        self._nome = nome
        self._raca = raca

    @property
    def nome(self):
        return self._nome

    @property
    def raca(self):
        return self._raca


felix = Gato('Felix', 'Vira-Lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)


# Fazendo a criação de um jsonpickle

poetry add jsonpickle


import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self._nome = nome
        self._raca = raca

    @property
    def nome(self):
        return self._nome

    @property
    def raca(self):
        return self._raca


felix = Gato('Felix', 'Vira-Lata')

ret = jsonpickle.encode(felix)
print(ret)

with open('arquivos/felix.json', 'w') as file:
    ret = jsonpickle.encode(felix)
    file.write(ret)



# Lendo um jsonpickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self._nome = nome
        self._raca = raca

    @property
    def nome(self):
        return self._nome

    @property
    def raca(self):
        return self._raca


felix = Gato('Felix', 'Vira-Lata')

with open('arquivos/felix.json', 'r') as file:
    content = file.read()
    ret = jsonpickle.decode(content)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
"""
