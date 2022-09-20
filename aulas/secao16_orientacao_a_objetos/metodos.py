"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja,
as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos em dois grupos:

- Métodos de Instância;
- Métodos de Classe;


Métodos de Instância:

- O método __init__ é um método especial chamado de Construtor e sua função
é construir o objeto a partir da classe.

# OBS: tod0 objeto em Python que inicia e finaliza com duplo underline é
chamado de dunder (Double UNDERline).

# OBS: Os métodos/funções dunder em Python
são chamados de Métodos Mágicos.

ATENÇÃO! Por mais que possamos criar nossas própria funções utilizando dunder,
__exemplo__, não é aconselhado. Python possui vários métodos com esta forma de
nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas
internas da linguagem, então EVITE AO MÁXIMO, de preferência NUNCA O FAÇA.

# Métodos são escritos em letras minúsculas, se o nome for composto será separado
por underline "_".


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcetagem):
        ""Retorna o valor do produto com desconto""
        return (self.__valor * (100 - porcetagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema.')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def ver(self):
        print('teste')


# p1 = Produto('Playstation 4', 'Video Game', 2300)

# print(p1.desconto(20))
# print(Produto.desconto(p1, 20))

# user1 = Usuario('Angelina', 'Jolie', 'angelinajolie@gmail.com', '123456')
# user2 = Usuario('Felicity', 'Jones', 'felicityjones@gmail.com', '654321')

# print(user1.nome_completo())
# print(user2.nome_completo())
# print(Usuario.nome_completo(user1))

# Acesso indevido:

# print(f'Senha user1: {user1._Usuario__senha}')
# print(f'Senha user2: {user2._Usuario__senha}')

# nome = input('Informe o nome:\n-> ')
# sobrenome = input('Informe o sobrenome:\n-> ')
# email = input('Informe o email:\n-> ')
# senha = input('Informe o senha:\n-> ')
# confirma_senha = input('Confirme a senha:\n-> ')

# if senha == confirma_senha:
#     user = Usuario(nome, sobrenome, email, senha)
# else:
#     print('Senha não confere...')
#     exit(1)

# print('Usuário criado com sucesso!')

# senha = input('Informe a senha para acesso:\n-> ')

# if user.checa_senha(senha):
#     print('Acesso permitido!')
# else:
#     print('Acesso negado!')

# print(f'Senha criptografada: {user._Usuario__senha}.')  # Acesso errado.


# Métodos de classes:

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possível, mas incorreta

# Métodos de Classe, em Python, são conhecidos como Métodos Estáticos em
# outras linguagens.
"""
