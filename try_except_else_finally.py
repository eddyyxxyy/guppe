"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DO USUÁRIO DEVE SER TRATADA!

OBS: a função do usuário é DESTRUIR seu sistema.


# Else: é executado somente se não ocorrer a exceção/erro.
# Para cada except podemos ter um else.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou: {num}')


# Finally:

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: o bloco finally é sempre executado, independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos. Como para fechar um serviço SQL ou arquivo
# que tenhamos aberto para realizar as operações do código criado.



# Exemplo mais complexo ERRADO:


def div(n1, n2):
    return n1 / n2


num1 = int(input('Informe o primeiro número: '))
try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print("O valor precisa ser númerico")

try:
    print(div(num1, num2))
except NameError:
    print('Valor incorreto')


# Exemplo mais complexo CORRETO:
# Você é responsável pelas entradas de suas funções. Então, TRATE-AS!


def div(n1, n2):
    try:
        return int(n1) / int(n2)
    except ValueError:
        return 'Valor incorreto!'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero!'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(div(num1, num2))


# Exemplo mais complexo com tratamento genérico:
# Você é responsável pelas entradas de suas funções. Então, TRATE-AS!


def div(n1, n2):
    try:
        return int(n1) / int(n2)
    except:
        return 'Ocorreu um problema!'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(div(num1, num2))


# Exemplo mais complexo com tratamento semi-genérico:
# Você é responsável pelas entradas de suas funções. Então, TRATE-AS!


def div(n1, n2):
    try:
        return int(n1) / int(n2)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema! {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(div(num1, num2))

"""
