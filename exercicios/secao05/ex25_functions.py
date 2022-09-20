def raizes(a: float, b: float, c: float):
    """Takes in 3 args and calculate x1 and x2"""
    D = b**2 - 4 * a * c
    x1 = (-b + D ** (1 / 2)) / (2 * a)
    x2 = (-b - D ** (1 / 2)) / (2 * a)
    print(f'Valor de delta: {D}')
    if D < 0:
        print('\nNão existe raiz real!')
        print(f'Valor de x1: {x1}')
        print(f'Valor de x2: {x2}')
    if D > 0:
        print('\nDuas raízes:')
        print(f'Valor de x1: {x1}')
        print(f'Valor de x2: {x2}')
    elif D == 0:
        print(f'Raiz única: ', end='')
        if (x1 is float) and (x2 is not float):
            print(x1)
        elif (x1 is not float) and (x2 is not float):
            print(x2)
