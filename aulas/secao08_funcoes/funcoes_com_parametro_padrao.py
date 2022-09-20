"""
Funções com parâmetros padrões (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional (Built-in):

print()

print('Geek University')

OU (Declaração da função pelo programador):


def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))  # Por padrão eleva ao quadrado
print(exponencial(3, 5))  # Eleva ao número informado (pelo usuário, seu argumento) para o parâmetro potencia


# Exemplo de função onde a passagem de parâmetro é obrigatória:


def quadrado(n):
    return n * 2


print(quadrado(3))
print(quadrado())

OBS: Em funções Python, os parâmetros com valor padrão, parâmetros Default, devem SEMPRE estar após os valores obriga-
tórios, NUNCA antes, pois dá erro de SyntaxError.


Por que usar funções com parâmetros com valor Default:
- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos e/ou não informados;
- Nos permite trabalhar com exemplos mais legíveis de código;


Quais tipos de dados podemos usar como valores default para parâmetros:
- Qualquer tipo de dado, entre eles:
    ints, strings, floats, booleanos, listas, tuplas, dicionários, funções, etc...

# A exemplo das duas ultimas explicações:


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(2, 3))
print(mat(2, 2, subtracao))


Escopo - Evitar problemas e confusões...
- Variáveis globais;
- Variáveis locais.

Exemplo:

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi, {instrutor}!'


print(diz_oi())

# Se tivermos uma variável local com o mesmo nome de uma
# variável global, a local terá preferência.

# ATENÇÃO COM VARIÁVEIS GLOBAIS (se puder evitar, evite!)

total = 0


def incrementa():
    total += 1  # UnboundLocalError (A variável está sendo usada para processamento sem ter sido inicializada)
    return total


print(incrementa())

CORRIGINDO o código acima:

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global.
    total += 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())


Podemos ter funções que são declaradas dentro de funções, que também tem uma forma especial de escopo de variável
"""


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador

    return dentro()
