"""
Lendo arquivos CSV

CSV: Comma Separeted Values - Valores Separados por Vírgula

# Separador por vírgula

1, 2, 3, 4, 5, 6

"geek", "university", "python", "ciência"

# Separador por ponto e vírgula

1; 2; 3; 4; 5; 6

"geek"; "university"; "python"; "ciência"

# Separador por espaço

1 2 3 4 5 6

"geek" "university" "python" "ciência"


Podemos ter qualquer caractere como separador, desde que seja o
mesmo em tod0 arquivo.

https://dados.gov.br/dataset


# Possível de se trabalhar, mas não é o ideal
with open('arquivos/lutadores.csv') as lut:
    dados = lut.read()
    dados = dados.split(',')[2:]
    print(dados)


A linguagem Python possui duas formas diferentes para ler
dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do
    arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do
    arquivo CSV como Ordered Dicts.



# Reader

from csv import reader

with open('arquivos/lutadores.csv') as file:
    file_reader = reader(file)  # Atribui um iterator
    next(file_reader)  # Pula cabeçalho
    for row in file_reader:
        # Cada linha é uma lista:
        print(f'{row[0]} nasceu no(a)(s) {row[1]} e mede {row[2]}cm de altura')



# DictReader

from csv import DictReader

with open('arquivos/lutadores.csv') as file:
    file_reader = DictReader(file)
    next(file_reader)
    for row in file_reader:
        # Cada linha é um OrderedDict
        print(f"{row['Nome']} nasceu no(a)(s) {row['País']} e tem {row['Altura (em cm)']}cm de altura")
"""

# DictReader

from csv import DictReader

with open('arquivos/lutadores.csv') as file:
    file_reader = DictReader(file, delimiter=',')
    next(file_reader)
    for row in file_reader:
        # Cada linha é um OrderedDict
        print(
            f"{row['Nome']} nasceu no(a)(s) {row['País']} e tem {row['Altura (em cm)']}cm de altura"
        )
