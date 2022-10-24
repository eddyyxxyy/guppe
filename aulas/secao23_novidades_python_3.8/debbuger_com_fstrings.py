"""
Debugger mais simples com f-strings


def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2


resultado: float = multiplicar(4.2345, 6.7890)

print(f'O resultado é {resultado}')
print(f'O resultado é {multiplicar(4.2345, 6.7890):.2f}')
print(f'O resultado é {(resultado := multiplicar(4.2345, 6.7890)):.2f}'
      f' é a metade de media {resultado * 2}')

geek: str = 'Geek University'

print(f"geek='{geek}'")
print(f'{geek=}')
print(f'{geek.upper()[::-1] = }')
"""
