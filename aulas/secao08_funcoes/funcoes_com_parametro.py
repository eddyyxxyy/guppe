"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processados
dentro da mesma;

Se pensarmos em um programa qualquer, geralmente temos:
Entrada → Processamento → Saída
Logo, se persarmos em uma função, já sabemos que temos
    funções que não possuem entrada, não possuem saída,
    possuem entrada mas não possuem saída, não possuem
    entrada, mas possuem saída e outras que possuem entrada
    e saída.

Exemplo de função com parâmetro de entrada:

def quadrado(n):
    return n * n


print(quadrado(2))  # Imprimirá o valor 4 neste exemplo.


# Em uma função, podemos receber quantos parâmetros forem necessários,
e eles são separados por vírgula...

OBS: Em funções com parâmetros obrigatórios, se passarmos mais ou menos parâmetros
necessários para a execução da função, teremos TypeError;


A diferença entre parâmetros e argumentos:
- Parâmetros são variáveis declaradas na definição de uma função;
- Argumentos são dados passados durante a execução de uma função;

Exemplo:
   Parâmetros
      ↓  ↓
def a(b, c):
    pass


Argumentos
  ↓  ↓
a(5, 4)

OBS: a ordem dos parâmetros importa;


Argumentos nomeados (Keyword Arguments):
- Caso utilizemos os nomes dos parâmetros nos argumentos para informá-los
podemos utilizar qualquer ordem;


Erro comum na utilização de return é colocar o return no local errado,
finalizando a função antes do momento esperado, retornando valores equivocos.
"""
