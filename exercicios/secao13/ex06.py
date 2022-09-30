"""
6) Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
vezes cada letra do alfabeto aparece dentro do arquivo.
"""
from string import ascii_lowercase


def count_letters(path: str) -> int:
    count = 0
    with open(path, mode='r', encoding='UTF-8') as f:
        text = f.read()
        for letter in text:
            if letter.lower() in ascii_lowercase:
                count += 1
    return count


def main() -> None:
    result = count_letters('arquivos/ex06_arq.txt')
    print(f'Amount of letters in file: {result}')


if __name__ == '__main__':
    main()
