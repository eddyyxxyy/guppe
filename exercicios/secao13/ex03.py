"""
3) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas letras são vogais.
"""


def count_vowels(path: str) -> int:
    count = 0
    with open(path, 'r', encoding='UTF-8') as arq:
        for char in arq.read():
            if char.lower() in 'aeiou':
                count += 1
    return count


def main() -> None:
    result = count_vowels('arquivos/ex03_arq.txt')
    print(f'Amount of vowels in the txt file: {result}')


if __name__ == '__main__':
    main()
