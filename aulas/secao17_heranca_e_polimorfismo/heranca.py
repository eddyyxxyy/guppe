"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código, mas não só isso. Também existe para
extender as nossas classes.

OBS: Com a Herança, à partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente:
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario:
    - nome;
    - sobrenome;
    - cpf;
    - matricula;


Existe alguma entidade genérica o suficiente para encapsular os atributos
e métodos comuns à outras entidades?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


OBS: quando uma Classe herda de outra Classe, ela herda todos os atributos e métodos
da Classe herdada.

Quando uma Classe herda de outra Classe, a classe herdada é conhecida por:
    (No nosso caso, a classe Pessoa, definida abaixo da explicação)
    - Super Classe;
    - Classe Pai;
    - Classe Mãe;
    - Classe Base;
    - Classe Genérica;
Quando uma Classe herda de outra Classe, ela é chamada de:
    (Nesse caso a classe Cliente e Funcionario)
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    '''Cliente henda de pessoa'''

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    '''Funcionário henda de pessoa'''

    def __init__(self, nome, sobrenome, cpf,  matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


# Sobrescrita de Métodos (Overriding)

Sobrescrita de Métodos ocorre quando reimplementamos um método presente
na Super Classe em Classes filhas.
"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente henda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário henda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
