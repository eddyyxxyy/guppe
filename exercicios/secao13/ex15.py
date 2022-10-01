"""
15) Faça um programa que receba como entrada o ano corrente e o nome de dois
arquivos: um de entrada e outro de saída. Cada linha do arquivo de entrada
contém o nome de uma pessoa (ocupando 40 caracteres) e o seu ano de nascimento.
O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece
o nome da pessoa seguida por uma string que representa a sua idade.
    . Se a idade for menor do que 18 anos, escreva "menor de idade"
    . Se a idade for maior do que 18 anos, escreva "maior de idade
    . Se a idade for igual a 18 anos, escreva "entrando na maior idade"
"""


def main() -> None:
    year = int(input('Enter the current year: '))
    path_file0 = str(input('Path to read the file: '))
    path_file1 = str(input('Path to write new file: '))

    with open(path_file0) as f0, open(path_file1, 'w') as f1:
        for row in f0.readlines():
            born = int(row[40:])
            age = year - born
            if age == 18:
                result = f'{row[:40]}{age} - coming of age\n'
                f1.write(result)
            elif age > 18:
                result = f'{row[:40]}{age} - adult\n'
                f1.write(result)
            else:
                result = f'{row[:40]}{age} - minor\n'
                f1.write(result)


if __name__ == '__main__':
    main()
