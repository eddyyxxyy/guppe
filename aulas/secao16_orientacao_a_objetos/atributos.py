"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto, ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em três grupos:
    -> Atributos de instância;
    -> Atributos de Classe;
    -> Atributos dinâmicos.


# Atributo de instância: São atributos declarados dentro do método construtor*
    * Método construtor é um método especial utilizado para a construção do objeto.


# Em java, uma classe Lampada, incluindo seus atributos ficaria, mais ou menos, assim:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor, Boolean ligada){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

# Em Python, por convenção, ficou estabelecido que tod0 Atributo de uma Classe
é Público, ou seja, pode ser acessado em tod0 o projeto.
Caso queiramos demonstrar que determinado Atributo deve ser tratado como Privado,
ou seja, que deve ser acessado/utilizado somente dentro da própria Classe, onde
está declarado, utiliza-se duplo underscore no ínicio de seu nome.
Isso é conhecido também como Name Mangling.


# Classes com Atributos de Instância Públicos.
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos públicos e Atributos privados:

class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.__email)


# OBS: Lembre-se que isso é somente por convenção, o Python não vai
# impedir que façamos acesso aos atributos sinalizados como privados
# fora da classe.

user = Acesso('user@gmail.com', '123456')

# Acesso com Name Mangling (NÃO FAÇA):

# print(user.__senha)  # AttributeError

# Temos acesso, mas não deveríamos o fazer, pois é Name Mangling (que é a
# junção do nome da Classe com o Atributo Privado.

# print(user._Acesso__senha)  # Assim podemos fazer o acesso, mas não é o correto,
# de toda forma, se necessário há como fazê-lo.

# Como fazer acesso sem Name Mangling:

user.mostra_email()
user.mostra_senha()

# O que significa Atributos de Instância?

# Significa que ao criarmos Instâncias/Objetos de uma Classe, todas as Instâncias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

# Acima temos duas Instâncias, ambos tem os atributos da Classe. Mesmo sendo
# diferentes eles compartilham essa característica.

user1.mostra_email()
user2.mostra_email()


# Atributos de Classe:

# Atributos de Classe são Atributos que são declarados diretamente na Classe,
# ou seja, fora do construtor. Geralmente já inicializamos um valor e este valor
# é compartilhado entre todas as Intâncias da Classe, ou seja, ao invés de cada
# Instância da Classe ter seus próprios valores como é o caso dos Atributos de
# Instância, com os Atributos de Classe todas as Instâncias terão o mesmo valor
# para este Atributo.

# Refatorando a Classe Produto


class Produto:
    # Atributo de Classe:
    imposto = 1.05  # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('PlayStation', 'Video Game', 2300)
p2 = Produto('Xbox Series X', 'Video Game', 4500)

# O valor mostrado agora é com o imposto já aplicado sobre o valor.
print(p1.imposto)  # Acesso incorreto ao Atributo de Classe
print(p2.imposto)  # Acesso incorreto ao Atributo de Classe

# OBS: Não precisamos criar uma Instância de uma Classe para fazer
# acesso à um Atributo de Classe.

print(Produto.imposto)  # Acesso correto ao Atributo de Classe

# Diretamente através da Classe, podemos fazer acesso ao seu Atributo,
# pois como o próprio nome diz, é um Atributo DE CLASSE, DA CLASSE.

print(p1.id)
print(p2.id)

# OBS: Em linguagens como Java, os Atributos de Classe do Python são
# chamados de Atributos Estáticos.


# Atributos Dinâmicos -> Um Atributo de Instância que pode ser criado
# em tempo de execução.

# OBS: O Atributo Dinâmico será exclusivo da Instância que o criou.

p1 = Produto('PlayStation', 'Video Game', 2300)
p2 = Produto('Xbox Series X', 'Video Game', 4500)

# Criando um Atributo Dinâmico em tempo de execução:

p2.peso = '5kg'
# Note que na Classe Produto, não existe o Atributo
# de Instância Peso.

print(
    f'\nProduto: {p2.nome};'
    f'\nDescrição: {p2.descricao};'
    f'\nPeso: {p2.peso};'
    f'\nValor: {p2.valor}.'
)

print(
    f'\nProduto: {p1.nome};'
    f'\nDescrição: {p1.descricao};'
    # f'\nPeso: {p1.peso};'  # Dá erro, pois não foi atribuido dinamicamente na Instância e nem na Classe
    f'\nValor: {p1.valor}.\n'
)

# Deletando atributos:

print(p1.__dict__)
print(p2.__dict__)
# print(Produto.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)
"""
