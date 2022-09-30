"""
10) Faça um programa que receba o nome de um arquivo de entrada e outro de saída.
O arquivo de entrada contém em cada linha o nome de uma cidade (ocupando 40
caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de
entrada e gerar um arquivo de saída onde aparece o nome da cidade mais populosa
seguida pelo seu número de habitantes.
"""


def main() -> None:
    with open('arquivos/ex10_arq0.txt') as f, \
            open('arquivos/ex10_new_arq.txt', 'w') as f1:
        rows = f.readlines()
        populated = max(rows, key=lambda population: int(population[40::]))
        f1.write(populated)


if __name__ == '__main__':
    main()


"""
# Primeira solução do ex:

def main() -> None:
    result = 0
    with open('arquivos/ex10_arq0.txt') as f, \
            open('arquivos/ex10_new_arq.txt', 'w') as f1:
        rows = f.readlines()
        result = rows[0]
        for row in rows:
            result = row if float(row[40:]) > float(result[40:]) else result
        f1.write(result)


if __name__ == '__main__':
    main()
"""