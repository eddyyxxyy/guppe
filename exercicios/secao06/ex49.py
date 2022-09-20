"""
49) O funcionátios chamado Carlos tem um colega chamado João
que recebe um salário que equivale a um terço do seu salário. Carlos
gosta de fazer aplicações na caderneta de poupança e vai aplicar seu
salário integralmente nela, pois está rendendo 2% ao mês. João aplicará
seu salário integralmente no fundo de renda fixa, que está rendendo 5%
ao mes. Construa um programa que deverá calcular e mostrar a quantidade
de meses necessários para que o valor pertencente a João iguale ou ultrapasse
o valor pertencente a Carlos. Teste com outros valores as taxas.
"""


def calc_salary() -> tuple:
    carlos = 1000
    joao = carlos / 3
    contador = 0
    while True:
        if joao >= carlos:
            break
        carlos = carlos * 1.02
        joao = joao * 1.05
        contador += 1
    return carlos, joao, contador


def main() -> None:
    networth = calc_salary()
    print(networth)
    print(
        'How many months does it take for Carlos, receiving R$1000.00 and \n'
        'earning 2% per month, to be surpassed by João, who receives one third \n'
        "of Carlos' salary, earning 5% per month?"
        '\nFor João to have a cash value greater than Carlos, are necessary:'
        f'\n-> {networth[2]} months.'
    )


if __name__ == '__main__':
    main()
