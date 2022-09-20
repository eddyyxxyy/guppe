"""
O bloco Try/Except

# Em outras linguagens, conhecemos o Try/Except como Try/Get

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código, previnindo que o programa pare de
funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //Execução problemática
except:
    //O que deve ser feito em caso de problemas


# Exemplo 1: tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Estamos basicamente falando para o Python:
# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.
# O try/except pega qualquer tipo de erro genérico

try:
    len(5)
except:
    print('Deu algum problema')

OBS: tratar erro de forma genérica, não é a melhor maneira de se lidar com o tratamento de erros. O ideal é sempre
tratar de forma específica


# Exemplo para tratar um erro específico:

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')


try:
    len(5)
except TypeError:
    print('Você está utilizando um valor do tipo errado para o len()')


# Exemplo com detalhes do erro, dando um 'apelido' ao erro:

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')


# Podemos tratar diversos tratamentos de erro de uma vez:

try:
    # len(5)
    geek()
    # print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print(f'Deu um erro diferente')


# Exemplo com função que trata os potenciais erros:


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Geek'}

# print(pega_valor(dic, 'nome'))
# print(pega_valor(dic, 'batata'))
print(pega_valor(dic, 8))
"""
