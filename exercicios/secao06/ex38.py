"""
38) Faça um programa que calcule o terno pitagórico a, b, c, para o qual
a + b + c = 1000. Um termo pitagórico é um conjunto de três números
naturais, a, b, c, para a qual,
    a² + b² = c²
Por exemplo,
    3² + 4² = 5²
"""


def find_pitagorian_terms_of_1000():
    for a in range(500):
        for b in range(a + 1, 500):
            c = 1000 - (a + b)
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c


def main():
    numbers = find_pitagorian_terms_of_1000()
    print(
        'Pythagorean triplet terms that add up to 1000:'
        f'\n-> {numbers}'
    )


if __name__ == '__main__':
    main()
