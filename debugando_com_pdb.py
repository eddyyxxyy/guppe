"""
Debugando com PDB - Python Debugger

OBS: A utilização do print() para debugar código é uma prática ruim, pois existem formas melhores.
Exemplo de prática ruim:


def dividir(n1, n2):
    print(f'a={n1} b={n2}')
    try:
        return int(n1) / int(n2)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema! {err}'


print(dividir(4, 7))


Existem formas mais profissionais de se fazer o "debug", utilizando o PDB, Python Debugger. Em Python podemos fazer
isso em diferentes IDEs, ou utilizando o PDB mesmo.

# Exemplo com o PyCharm


def dividir(n1, n2):
    try:
        return int(n1) / int(n2)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema! {err}'


print(dividir(4, 0))


# Exemplo com PDB:

# Para utilizar o Python Debbuger, precisamos* importar a biblioteca PDB e então utilizar a função set_trace()

# A partir Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como
# função built-in (integrada), chamada breakpoint().

# Comandos básicos do PDB:
- l para listar onde estamos no código
- n para próxima linha
- p imprimi variável
- c continua a execução ou finaliza o debugging

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'faz o curso' + curso
print(final)

# Forma melhor:

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'faz o curso' + curso
print(final)

# Por que utilizar este formato? O Debug é utilizado durante o desenvolvimento, costumamos realizar todos os imports
# no início do arquivo. Por isso, ao invés de colocarmos o import no início do código, o colocamos logo durante a
# codificação para posteriormente removê-lo.
# OBS: quando queremos realizar dois comandos Python na mesma linha, usamos ponto e vírgula.

# Forma melhor ainda, e atual:


nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)


# OBS: Cuidado com conflitos entre os nomes de variáveis e os comandos pdb, tendo variáveis com o nome igual ao
# comando pdb. Por isso podemos utilizar o comando p, para imprimir uma variável com o mesmo nome das funções do pdb
"""
