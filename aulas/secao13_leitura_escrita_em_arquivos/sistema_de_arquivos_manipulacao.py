"""
Sistema de Arquivos - Manipulação



# Descobrindo se um arquivo ou diretório existe:

# Arquivo
print(os.path.exists('arquivo.txt'))  # False, pois não existe esse arquivo.
print(os.path.exists('frutas.txt'))  # True


# Diretório

# Paths relativos:
print(os.path.exists('aulas'))  # False pois não existe a pasta aulas dentro da pasta aulas
os.chdir('..')  # Saindo do dir aulas
print(os.path.exists('geek'))  # True, pois saímos do dir aulas e estamos agora perguntando se há dir geek no dir guppe
print(os.path.exists('geek\\university\\geek3.py'))  # True

# Paths absolutos:
print(os.path.exists('D:\\Estudos\\GeekUniversity\\PythonBasicoAoAvancado'))  # True
print(os.path.exists('D:\\Estudos\\GeekUniversity\\PythonBasicoAoAvancado\\PEP9'))  # False, não há PEP9 como dir


# Criando arquivos:

# Forma 1:
open('arquivo-teste.txt', 'w').close()

# Forma 2:
open('arquivo-teste2.txt', 'a').close()

# Forma 3:

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Forma 4

# os.mknod('arquivo-teste4.txt')  # Não funciona no Windows, somente em sistemas posix
with open('arquivo-teste4.txt', 'a') as arquivo:
    pass

# OBS: Se você estiver no Mac OS, pode haver um erro de PermissionError
# OBS: Se criando um arquivo via mknod com o arquivo já existente, teremos o erro FileExistsError


# Criando diretórios - únicos, um a um:

os.mkdir('templates')
# OBS: Se o diretório já existir, dará FileExistsError
# OBS: Se não tivermos permissão para criar o diretório, teremos um PermissionError


# Criando diretórios - multiplos, árvore de diretórios:

os.makedirs('templates\\geek\\university')
# OBS: Se já existirem os diretórios, dará FileExistsError


os.makedirs('templates\\geek\\university', exist_ok=True)
# Fará com que o erro causado caso os diretórios já existam (FileExistsError) não ocorra, pois irá ignorar o processo.


# Renomear arquivos e diretórios

# Diretórios:

os.rename('templates', 'templates2')
# OBS: se o diretório não existir, teremos FileNotFoundError
# OBS: se o diretório que queremos renomear não estiver vazio, teremos OSError


# Arquivos:

os.rename('templates2\\geek\\university\\teste.txt', 'teste2.txt')
# ATENÇÃO: O arquivo 'teste.txt' foi deletado

os.rename('templates2\\geek\\university\\texte.txt', 'templates2\\geek\\university\\texte2.txt')
# OBS: Agora sim o arquivo foi renomeado em vez de deletado, é necessário informar tod0 o caminho


# Removendo arquivos:

# ATENÇÃO: tome cuidado com os comandos de deleção!
# Ao deletarmos um arquivo ou diretório eles não vão para a lixeira, eles somem.

os.remove('nome_do_arquivo')

# OBS: se você estiver no Windows e o arquivo que for deletar estiver em uso, você terá um erro.
# OBS: caso o arquivo não exista, teremos o FileNotFoundError.
# OBS: se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError.


# Removendo diretórios:

# ATENÇÃO: tome cuidado com os comandos de deleção!
# Ao deletarmos um arquivo ou diretório eles não vão para a lixeira, eles somem.

os.rmdir('nome_do_diretorio')

# OBS: caso o diretório não esteja vazio, teremos OSError.
# OBS: caso o diretório não exista, teremos FileNotFoundError.


# Removendo uma árvore de diretórios:

os.removedirs('diretorio\\diretorio2')
# OBS: Remove ambos os diretórios, o raiz e o diretório dentro dele
# OBS: Se algum dos diretórios contiver arquivos ou outros diretórios o processo para



# Trabalhando com arquivos e diretórios temporários

import os
import tempfile


# Diretórios temporários:

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em tmp')
    with open(os.path.join(tmp, 'arquivo_temporário.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando o arquivo_temporario em modo de escrita
# no final utilizamos o input somente para manter os arquivos temporários "vivos" e podermos verificar dentro da pasta.

# OBS: possivelmente o código acima não irá funcionar se você estiver utilizando o windows. Por conta desse sistema
# trabalhar de forma diferente com arquivos temporários.


# Arquivos temporários:

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b''.
"""
