"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional,
precisamos importar e fazer uso do módulo os.

OS -> Operating System - Sistema Operacional


# Fazendo o import:
import os


# getcwd() -> Pega o current work directory -> Diretório de trabalho corrente,
# ou seja, onde você está!

print(os.getcwd())  # Retorna o path (caminho) absoluto.
# D:\\Estudos\\GeekUniversity\\PythonBasicoAoAvancado\\Projetos\\guppe\\aulas - > Caminho absoluto.

# Para mudar o diretório, podemos utilizar o chdir():

os.chdir('..')  # Vai para o diretório anterior ao que se está.

# D:\\Estudos\\GeekUniversity\\PythonBasicoAoAvancado\\Projetos\\guppe -> Caminho anterior ao dir /aulas
print(os.getcwd())


# Podemos checar se um diretório é absoluto ou relativo:

print(os.path.isabs(''))

# OBS para usuários Windows: se você estiver utilizando um computador com Windows,
# terá de tomar cuidado ao verificar diretórios:

print(os.path.isabs('C:\\Users\\edson'))

# O uso do caractere de Escape nos força a utiliza-lo duas vezes, a duplicidade
# informa que o próximo caractere é de fato um separador, o mesmo serve para
# quando vamos imprimir algo, para escrever uma única contra-barra é necessário
# informar duas.

print('Geek \\ University')



# Podemos identificar o sistema operacional:

print(os.name)  # posix (Linux e Mac) & nt (Windows)

# Podemos ter mais detalhes:

# print(os.uname())

# OBS para Windows: temos mais um problema, uname só funcionará com o
# módulo platform, então importe-o caso estiver no Windows.

import platform

print(platform.uname())


# Usando os.path.join() para navegar entre os diretórios.

print(os.getcwd())  # D:\\Estudos\\GeekUniversity\\PythonBasicoAoAvancado\\Projetos\\guppe\\aulas

res = os.path.join(os.getcwd(), '..', 'geek', 'university')
# '..' para sair do dir aulas e os outros dois parâmetros para acessar o diretório geek e então university.

os.chdir(res)

print(os.getcwd())  # D:\\Estudos\\GeekUniversity\\PythonBasicoAoAvancado\\Projetos\\guppe\\geek\\university

# Veja que o os.path.join() recebe por padrão dois parâmetros, sendo o primeiro o dir atual e os outros
# são os diretórios que serão juntados ao atual.


# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir())  # Diretório atual do arquivo é o padrão, ou seja, no diretório aulas para este arquivo
print(len(os.listdir()))  # Quantidade de arquivos dentro do dir aulas

print(os.listdir('D:\\Estudos\\GeekUniversity\\PythonBasicoAoAvancado\\Projetos\\guppe'))  # Diretório informado como
# parâmetro


# Podemos listar os arquivos e diretórios com mais detalhes, utilizando o os.scandir()

print(list(os.scandir()))  # Diretório atual do arquivo é o padrão, ou seja, no diretório aulas para este arquivo

print(list(os.scandir('D:\\Estudos\\GeekUniversity\\PythonBasicoAoAvancado\\Projetos\\guppe')))  # Diretório informado
# como parâmetro

# Aprofundando:

scanner = os.scandir()
arquivo = list(scanner)

print(arquivo[0].inode())  # Identificador de node na árvore de diretórios
print(arquivo[0].is_dir())  # É diretório? False
print(arquivo[0].is_file())  # É um arquivo? True
print(arquivo[0].is_symlink())  # É um link simbólico? False
print(arquivo[0].name)  # Nome do arquivo
print(arquivo[0].path)  # Caminho até o arquivo
print(arquivo[0].stat())  # Estatísticas sobre o arquivo

# OBS: Quando utilizamos a função scandir(), nós precisamos fechá-la, assim como quando abrimos um arquivo.

scanner.close()

"""
