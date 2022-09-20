"""
Escrevendo em arquivos

# OBS: ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler. Da mesma forma, se abrirmos
um arquivo para escrita, não podemos lê-lo, apenas escrever.

# OBS: ao abrir um arquivo para escrita que não existe ainda, o arquivo é criado no sistema operacional.

# OBS: Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write(), esta função recebe uma
string como parâmetro. Se for de outro tipo o dado inserido no write, teremos um TypeError.

# OBS: Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado, caso ele já exista, o
anterior será apagado e o novo será criado. Dessa forma, tod0 o conteúdo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' -> modo write (escrita):

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros.\n')
    arquivo.write('Mais linhas.')


with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)
"""
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta: str = (
            input('Informe uma fruta ou digite sair: ').strip().title()
        )
        if fruta != 'Sair':
            arquivo.write(fruta + '\n')
        else:
            break
