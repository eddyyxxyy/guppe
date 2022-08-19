"""
Erros mais comuns em Python

ATENÇÃO! → É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código!

Os erros mais comuns:

- SyntaxError: ocorre quando o Python encontra um erro de sintaxe, ou seja, você escreveu algo que o Python não
reconhece como parte da linguagem;

def funcao:
    print('Geek University')

# Está faltando os parênteses para declarar a função, a sintaxe correta inplica no uso de () junto ao nome da função.

None = 1

# None é um tipo em Python, uma palavra reservada, e atribuindo um valor à ela, não podemos utilizar uma palavra
reservada, se colacassemos outra palavra, por exemplo def, teriamos o SyntaxError.

return

# Return tem de ser usada dentro de uma função, logo, retorna SyntaxError.


- NameError: ocorre quando uma variável ou função não foi definida;

print(geek)

# Retorna NameError pois o nome 'geek' não foi definido previamente, estamos tentando imprimir algo que não existe.

geek()

# Também retorna NameError, pois essa função não existe.

a = 18
if a < 10:
    msg = 'É maior que 10'
print(msg)

# Retorna NameError, pois no escopo das variáveis, msg é uma variável local e se o bloco de código nunca é assionado
# (já que o a é maior que 10), msg nunca existirá, fazendo a linguagem retornar NameError. Para resolver isso poderíamos
# declarar que (antes da condicional), msg = ''.


- TypeError: ocorre quando uma função/operação/ação é aplicada a um tipo errado;

print(len(5))

# Retorna TypeError, pois estamos tentando aplicar uma função que opera sobre iteráveis, um número inteiro não é
# iterável, assim como uma lista vazia também retornaria o erro.

print('Geek' + [])

print('Geek' + 4)

# Não podemos concatenar tipos diferentes, se o valor 4 estivesse entre parenteses, consequentemente se tornando uma
# string, aí sim poderiamos concatenar.


- IndexError: ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um
índice inválido;

lista = ['Geek']
print(lista[1])
print(lista[0][4])

# Não podemos acessar elementos, ou elementos dentro de um elemento, informando um índice que não existe.


- ValueErro: ocorre quando uma função/operação built-in recebe um argumento com o tipo correto mas com valor
inapropriado;

print(int('Geek'))

# O cast int, espera receber um valor que possa ser convertido para inteiro, retornando ValueError, pois strings
não podem ser convertidas para int, o mesmo valeria se tentassemos dar cast para float.


- KeyError: ocorre quando tentamos acessar um dicionário com uma chave que não existe;

dicionario = {'a': 1}
print(dicionario['b'])

# Retorna KeyError, pois a chave 'b' não existe.


- AttributeError: ocorre quando uma variável não tem um atributo/função;

tupla = (11, 2, 31, 4)
print(tupla.sort())

# Retorna AttributeError, pois essa função sort() é um atributo de listas, não de tuplas.
# Para resolver isso, poderíamos utilizar o método sorted(tupla), pois este atributo é para qualquer dado.


- IndentationError: ocorre quando não respeitamos a identação do Python, que é de 4 espaços.

def funcao():
return 'Geek'

# Espera-se, por exemplo, na declaração de uma função, a identação após os dois pontos.

for i in range(10):
i + 1

# Mais uma vez, é esperado a identação de 4 espaços para a definição do bloco de código pertencente ao for.

OBS: Exceptions e Erros são sinônimos na programação.
OBS: Importante ler e prestar atenção na saída de erro, no Traceback.
"""
