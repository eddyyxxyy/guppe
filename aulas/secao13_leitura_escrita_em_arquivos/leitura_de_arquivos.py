"""
Leitura de Arquivos

Para ler um arquivo, ler o conteúdo de um arquivo, em Python, utilizamos a função integrada open(), que literalmente
significa 'abrir'.

open() → Na forma mais simples de utilização, nós passamos apenas um parâmetro de entrada, que neste caso é o nome /
caminho do arquivo à ser lido. Esta função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.
OBS: Todos os parâmetros são opcionais, menos o caminho do arquivo.

https://docs.python.org/3/library/functions.html#open

OBS: Por padrão, a função open() abre o arquivo para leitura, este arquivo deve existir ou então teremos o erro
FileNotFoundError.

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='utf-8'>

- name: nome do arquivo
- mode: modo do arquivo, ele está em r → read() → ler
- encoding: codificação do arquivo


# Exemplo

arquivo = open('texto.txt', 'r', encoding='utf-8')

# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, usamos a função read()

ret = arquivo.read()

print(type(ret))
print(ret)

# O read(), quando foi atribuído à variável ret, se torna uma única string. Tudo relacionado à strs podem ser aplicados.

# print(arquivo.read())

# O Python utiliza um recurso para trabalhar com arquivos chamado cursor, esse cursor funciona como o cursor de escrita
# que estamos utilizando inclusive para escrever este texto (elemento piscante).

# print(arquivo.read())  # Não exibe nada, pois o cursor está logo após o primeiro conteúdo lido.

# A função read() lê tod0 o conteúdo do arquivo, não somente a primeira linha.
# Então quando printamos mais de uma vez, o conteúdo já foi lido e não há mais como o ler sem abrir novamente.
"""
