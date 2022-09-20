"""
Ranges
- Precisamos conhecer o loop for para usar os ranges;
- Precisamos conhecer os ranges para trabalhar melhor os loops for;

Ranges são utilizados para gerar sequências numérias, não de forma
aleatória, mas sim de maneira especificada

range(valor_de_parada)
range(valor_de_ínicio, valor_de_parada)
range(valor_de_ínicio, valor_de_parada, passo)

OBS: Valor de parada não inclusive (Ínicio padrão em 0 e passo padrão
de 1 em 1)

# forma 1:

for num in range(11):
    print(num)

# forma 2:

for num in range(1, 11):
    print(num)

# forma 3:

for num in range(0, 21, 2):  # inclusive podemos inverter com (20, -1, -2)
    print(num)
"""
