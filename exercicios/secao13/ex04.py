"""
4) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas letras são vogais e quantas são consoantes
"""


def count_vowels_consonants(path: str) -> tuple[int, int]:
    count_vowels = 0
    count_consonants = 0
    with open(path, mode='r', encoding='UTF-8') as arq:
        for char in arq.read().lower():
            if char in 'aeiou':
                count_vowels += 1
            else:
                if char in 'bcdfghjklmnpqrstvwxyz':
                    count_consonants += 1
    return count_vowels, count_consonants


def main() -> None:
    result = count_vowels_consonants('arquivos/ex04_arq.txt')
    print(
        'Amount of vowels in file:'
        f'\n-> {result[0]}'
        '\nAmount of consonants in file:'
        f'\n-> {result[1]}'
    )


if __name__ == '__main__':
    main()
