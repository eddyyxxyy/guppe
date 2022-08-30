"""
Modos de abertura de arquivos

r -> Abre para leitura, é o padrão caso não seja declarado modo;
w -> Abre para escrita, sobrescreve caso o arquivo já exista;

x -> Abre para escrita somente se o arquivo não existir, caso contrário gera FileExistsError;
# Exemplo de modo 'x':
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo.\n')
except FileExistsError:
    print(f'O arquivo já existe!')


a -> Abre para escrita, adicionando o conteúdo ao final do arquivo;
# OBS: Abrindo no modo 'a', que é append, se o arquivo não existe será criado, caso exista o novo conteúdo será
adicionado ao final. Mesmo que usemos o seek(0), será sempre no final do arquivo, não controlamos o cursor.

# Exemplo de modo 'a':
with open('frutas.txt', 'a') as arq:
    while True:
        fruta = input('Informe uma fruta ou sair: ').strip().title()
        if fruta != 'Sair':
            arq.write(fruta + '\n')
        else:
            break

with open('outro.txt', 'a') as arq:
    arq.seek(0)
    arq.write('No topo!\n')
    arq.write('Nova linha.\n')
    arq.write('Mais uma linha.\n')

+ -> Abre para o modo de atualização, leitura e escrita. Utilizamos ele com os outros modos quando declaramos, não há
jeito de automaticamente colocar o texto no topo, com r/w nós substituímos os dados do arquivo, com o a adicionamos ao
final.


with open('outro.txt', 'a+') as arq:
    # arq.seek(0)
    arq.write('Novo topo!\n')
    arq.write('Nova linha.\n')
    arq.write('Mais uma linha.\n')

"""
