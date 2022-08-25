sb = float(input('Informe seu salário: \033[1;37mR$\033[m').strip().replace(',', '.'))
print(f'Seu salário após o calculo de impostos e acréssimos é: R${(sb * 1.05) - (sb - sb * 0.93)}')
