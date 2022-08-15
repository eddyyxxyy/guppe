"""
Funções com retorno

OBS: quando uma função não retorna nenhum valor, o retorno é None
OBS: refatorar é modificar o código, reescreve-lo, para melhora-lo
OBS: não precisamos necessariamente criar uma variável para receber
o retorno de uma função. Podemos passar a execução da função para outras
funções.

Exemplo:

def quadrado_de_7():
    return 7 * 7


# ret = quadrado_de_7()

# print(f'{ret}')

print(f'Retorno: {quadrado_de_7()}')


Sobre a palavra reservada "return":
- Ela finaliza a função, ou seja, ela sai da execução da funçõa;
- Podemos ter em uma função, diferentes "returns";
- Podemos em uma função, retornar qualquer tipo de dado e até mesmo
multiplos valores;
- Qualquer comando após o return não será executada;


Codificação desnecessária na utilização de retorn:
- Por exemplo, não é necessário o uso de else em algumas funções, pois
o return já finaliza a execução.
"""
