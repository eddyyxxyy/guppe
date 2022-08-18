"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissão:
    - Permissão de leitura para ler o arquivo;
    - Permissão de escrita para escrever o arquivo;

StringIO -> Utilizado para ler e criar arquivos em memória!


"""

# Primeiro fazemos o import

from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida, ou mesmo vázia, para inserirmos texto depois.

arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos sobre manipulação de arquivos:
print(arquivo.read())

# Repare que não foi criado nada no diretório guppe, pois o arquivo contendo a string está em memória.

# Escrevendo outro texto:
arquivo.write(' Outro texto')

# Podemos, inclusive, movimentar o cursor:
arquivo.seek(0)
print(arquivo.read())
