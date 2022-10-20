"""
Alocação e Gerência de Memória

Em nosso computador, temos diversos componentes.
Entre eles, a memória é uma peça chave para todo
o funcionamento da máquina.

A Memória RAM que é onde todos os programas e o
OS ficam em execução e, claro, o Python faz uma
"Limpeza", um gerenciamento da memória quando é
o caso.

------------------------------------------------

Abstração sobre alocação e gerenciamento:

Imagine que duas telas, uma de execução (onde de
fato iremos "codar") e uma tela de saída (onde
veremos os resultados daquilo que programamos).

Agora pense que você declarou uma variável x:

x = 10

O que o Python irá fazer? O que se entende dessa
declaração de variável quanto à memória?

O Python colocará uma variável / um objeto, "x"
apontando para o valor 10, que está em memória.

Tudo em Python é objeto, logo, quando "x" recebe
o valor "10", ele é reconhecido como int (inteiro).

Agora caso façamos o seguinte:

y = x

O Python, agora, criará uma nova variável/objeto,
"chamado" de "y" apontando para o mesmo "local"
que x aponta.

Ou seja, não é alocado um novo espaço em memória,
este espaço que contém o valor "10" está sendo
apontado para os dois objetos "x" e "y".

Dessa forma, podemos:

if (id(x) == id(y)):
    print('x e y referenciam o mesmo objeto/local na memória')

Em nossa tela de saída teriams então printado a
mensagem, pois de fato são objetos que referenciam
o mesmo objeto de memória.

Com isso, podemos concluir que não são alocados
dois espaços em memória para variáveis que possuem
um mesmo valor.

Se, em algum momento, fizermos isso:

x = x + 1
# ou, alternativamente, gerando o mesmo efeito
x += 1

O Python irá tirar o vínculo do objeto "x" com
o objeto de memória que armazena o valor "10"
e criará um novo "local" na memória, que agora
armazena "11" e aponta para "x".

O Python inteligentemente reutiliza os valores
já alocados em memória para apontar para novos
objetos que corresponder ao seu valor contido,
economizando espaço em memória.

------------------------------------------------

Agora, aprofundamento:

Visão geral:

Na Memória RAM, onde está em execução o OS, aplicativos
diversos e Memória compartilhada, teremos uma
divisão entre Memória Stack e Heap (lembrando, essas
divisões dentro da Memória RAM).

Então, pense que você construiu um programa chamado
"principal.py". Nele está contido uma declaração
de variável:

y = 5

Na Memória Stack, será criado um Frame (Stack
Frame) com o nome do seu programa e o que ele
contém, nesse caso a variável/objeto "y", e na
Memória Heap será alocado um espaço com o valor
correspondente de "y", ou seja, "5".

"Por baixo dos panos" o Python está apontando
o objeto contido no "principal.py" que está
contido no Stack Frame para o espaço alocado
na Memória Heap que contém o valor "5".

Confuso, não? Talvez faça mais sentido ler
estes textos acompanhando o pdf disponível
com as "ilustrações".


Pensemos agora nas seguintes funções:


def funcao1(x):
    x *= 2
    y = funcao2(x)
    return y


def funcao2(x):
    x += 1
    return x


E na seguinte declaração contida em
"principal.py":

y = 5
z = funcao1(y)

Quando passamos o valor de "y" para "z",
a "funcao1" é chamada recebendo "y", é
alocado na Memória Stack um Frame com o
nome da função que conterá o valor de "x"
(nesse caso, recebendo o valor de "y" * 2)
e será alocado na Memória Heap o valor
correspondente e apontado para o objeto,
o valor é "10".

Após isso, é dito que "y" (dentro do escopo
da função, não sendo o mesmo "y" do programa
princial) receberá o retorno da "funcao2" com o
parâmetro "x" (10), sendo alocado na Memória
Stack um espaço com o nome da funcao2, seus
objetos/variáveis/processos contidos e na Memória
Heap os valores que correspondem à esses objetos.

Então, o "x" da funcao2 será alocado em outro
espaço, que aponta para o valor "11" e assim
que o retornar para o "y" da funcao1, "desapa-
recerá" da memória. Agora, o "y" da funcao1
apontará para o mesmo valor já alocado de "x"
da funcao2 (isso ocorre de forma rápida, antes
da deleção do Frame de funcao2).

Ao retornar o valor de "y" na funcao1 para "z"
no programa principal, o Frame (o espaço alocado
na Memória Stack) também "sumirá" e fará com que
"z" em "principal.py" aponte para aquele mesmo
espaço que fora reservado antes para o valor "11"
e "y" continue apontando para o valor "5" (já que
no escopo do programa "principal.py" este valor
permaneceu estático, sem alterações em sua execução).

Mas há um detalhe, o valor "10" da funcao1,
alocado na Memória Heap durante a execução,
permanece lá, consumindo aquele espaço.

Porém, é nesse momento que entra em ação
o Garbage Collector, que no Python é
chamado de Reference Counting. Ele
procura pelo objetos sem referência,
conhecidos como Dead Objets, justamente
como este valor "10" que "sobrou" na memória
Heap, limpando-o da memória.

------------------------------------------------------------------------------------------------------------------------

Por fim, uma comparação entre Python, Java e C:


Operação/Processo        |               Python                |                  Java / C
-------------------------|-------------------------------------|--------------------------------------------------------
Declaração               |              x = 10                 |                 int x = 10;
Declaração do tipo       |        Dinamicamente tipado         |       Estáticamente tipado (obrigatório)
O que é o 10?            |    Objeto criado na Memória Heap    |   Dado primitivo em bytes, 4 em Java e 2 em C
O que x contém?          |       Referência ao Objeto 10       |     Local na memória onde 10 está armazenado
x = x + 1                |  x referenciado à um novo objeto 11 | x aponta para o mesmo local com o valor alterado pra 11
x = 10                   |  x aponta para o mesmo objeto de y  |      x e y apontam para locais diferentes
y = 10                   |  y aponta para o mesmo objeto de x  |      y e x apontam para locais diferentes

------------------------------------------------------------------------------------------------------------------------

Relembrando tudo agora:

- Métodos e variáveis são criadas na memória stack;
- Os objetos e instancias são criadas na memória heap;
- Um novo stack é criado durante a invocação de uma função ou método;
- Stacks são destuidas sempre que uma função ou método retorna valor;
- Garbage Collector é um mecanismo para limpar dead objects;

Qualquer erro na explicação, quanto ao uso errado dos termos,
por favor, apontem em uma issue no repositório.
"""
