"""
Seek e Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo.

# Exemplos:

arquivo = open('texto.txt')

print(arquivo.read())

# A função seek() é utilizada para movimentação do cursor pelo arquivo, ela recebe um parâmetro que indica onde queremos
# colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek() -> seek significa procurar

arquivo.seek(0)  # retornou o cursor para o primeiro elemento textual da str

print(arquivo.read())  # agora podemos ler novamente o arquivo




arquivo = open('texto.txt')

# readline() -> Função que lê o arquivo linha a linha

# print(arquivo.readline())  # A cada readline(), o cursor vai para a linha abaixo, no começo dela
# print(arquivo.readline())

ret = arquivo.readline()
print(type(ret))
print(ret)
print(ret.split(' '))




# Realizando o procedimento do exemplo, conseguimos saber quantas linhas tem o arquivo.

arquivo = open('texto.txt', mode='r', encoding='utf-8')

# readlines() -> Função que lê AS linhas, note que está no plural, cada linha sendo um item de uma lista de strs

linhas = arquivo.readlines()

print(linhas)

print(len(linhas))




# OBS: quando abrimos um arquivo com a função open(), é criada uma conexão entre o arquivo no disco do computador e o
seu programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão,
para isso utilizamos a função close().

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

arquivo = open('texto.txt', mode='r', encoding='utf-8')

2 - Trabalhar o arquivo;

print(arquivo.read())
...

3 - Fechar o arquivo.

arquivo.close()

# print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado, retornando True se tiver fechado e False caso
estiver aberto.

# OBS: se tentarmos manipular um arquivo após fecha-lo, teremos ValueError.
"""

arquivo = open('texto.txt')

# Com o read() podemos limitar a quantidade de caracteres à serem lidas, colocando o cursos exatamente após o cactere
# de parada.
print(arquivo.read(50))  # Limita aos primeiros 50 caracteres
