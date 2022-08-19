"""
Bloco With

Passos para trabalhar com arquivos:

# 1 - Abrimos o arquivo;
# 2 - Trabalhamos o arquivo;
# 3 - Fechamos o arquivo;

O bloco with é utilizado para criar um contexto de trabalho,
onde os recursos utilizados são fechados após o bloco with.

ATENÇÃO: O próprio with abre e fecha nosso arquivo, impedindo
o lock do sistema operacional quanto ao uso do arquivo.

Ele facilita o trabalho com arquivos, é a forma Pythônica de
manipular arquivos.


"""

# O bloco with

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)
