"""
21) Leia um valor de massa em libras e apresente-o convertido em quilogramas.
A fórmula de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""
# K = L * 0.45
mli = float(input('Informe o peso em libras: ').strip().replace(',', '.'))
print(f'O peso de {mli:.1f}li em corresponde a {mli * 0.45:.1f}kg.')
