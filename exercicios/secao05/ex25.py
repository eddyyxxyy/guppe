"""
25) Calcule as raízes da equação de 2° grau;
    Lembrando que:
    x = – b ± √∆
          2∙a
    Onde:
    ∆ = b² - 4ac
    E ax² + bx + c = 0 representa uma equeção de 2° grau.
A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem
"Não é equação de segundo grau."
    - Se ∆ < 0, não existe real. Imprima a mensagem Não existe raiz
    - Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
    - Se ∆ > 0,imprima as duas raízes reais.
"""
from ex25_functions import raizes

a = 0
b = 0
c = 0
if __name__ == '__main__':
    print('Calculando as raízes de uma equação de 2º grau\n')
    while True:
        try:
            a = float(
                input('Entre com o valor de a: ').strip().replace(',', '.')
            )
        except ValueError:
            print('Valor inválido!')
            continue
        else:
            if a == 0:
                print('Não é equação de segundo grau!')
                break
            while True:
                try:
                    b = float(
                        input('Entre com o valor de b: ')
                        .strip()
                        .replace(',', '.')
                    )
                except ValueError:
                    print('Valor inválido!')
                    continue
                else:
                    while True:
                        try:
                            c = float(
                                input('Entre com o valor de c: ')
                                .strip()
                                .replace(',', '.')
                            )
                        except ValueError:
                            print('Valor inválido!')
                            continue
                        else:
                            break
                break
        raizes(a, b, c)
        continua = input('Deseja sair? Digite q ou Enter para novo cálculo:')
        if continua == 'q':
            break
