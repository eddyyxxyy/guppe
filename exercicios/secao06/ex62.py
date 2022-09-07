"""
62) Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro,
cinco, então há 2 + 4 + 4 + 6 + 5 = 21 letras usadas no total. Faça um programa
que conte quantas letras seriam utilizadas se todos os números de 1 a 1000 (mil)
fossem escritos em palavras.
OBS: Não conte espaços ou hífens

# Foi instalado o pacote num2words para reduzir o código e fazê-lo funcionar
com maior facilidade.
"""
from locale import setlocale, LC_ALL, format_string

from num2words import num2words


def count_number_letters():
    result = 0
    for i in range(1, 1001):
        result += (len(''.join(''.join(num2words(i, lang='pt_BR').split('-')).split(' '))))
    return result


def main():
    setlocale(LC_ALL, 'pt-BR')
    print(
        'How many letters would be used to write from 1 to 1000? (pt-BR)'
        f'\n-> {format_string("%d", count_number_letters(), grouping=True)} letters.'
    )


if __name__ == '__main__':
    main()
