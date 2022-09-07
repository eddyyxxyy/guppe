"""
61) Faça um programa que calcule o maior número palíndromo feito
a partir do produto de dois números de 2 dígitos. Ex: O maior palíndromo feito
a partir do produto de dois números de dois dígitos é 9009 = 91*99
"""


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def largest_palindrome(smallest, largest):
    z = 0
    for x in range(largest, smallest, -1):
        for y in range(largest, smallest, -1):
            if is_palindrome(x*y):
                if x*y > z:
                    z = x*y
    return z


def main() -> None:
    palindrome = largest_palindrome(100, 999)
    print('Largest palindrome made from the product of two 3-digit numbers:', palindrome)


if __name__ == '__main__':
    main()
