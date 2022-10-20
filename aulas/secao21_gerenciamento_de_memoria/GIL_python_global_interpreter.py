"""
GIL - Global Python Interpreter Lock

O GIL é um mutex (ou lock) que permite que
apenas uma thread tome conta do interpretador
Python. Basta entendê-lo como algo que
bloqueará algo.

Ou seja, o GIL limita à somente uma thread
a execução do programa em qualquer ponto do
tempo.

Seu impacto não é visível para desenvolvedores
que executam programas single-thread, mas gera
problemas para programas que precisam de tempo
de resposta em códigos multi-thread.

Como em muitos computadores temos uma arquitetura
multi-threads, o GIL é visto como um aspecto de
antiquado no Python.

Entendendo seu funcionamento podemos então
compreender como isso afeta a performance de
nossos programas Python e como mitigar esse
problema.

--------------------------------------------------

Como pôde ser visto na aula sobre alocação e
gerenciamento de memória, o Python utiliza
um recurso chamado de Reference Counting, que
gerência os apontamentos dos objetos à seus
respetivos "resultados" dentro da memória
Heap.

Isso significa que tod0 objeto Python mantém
uma variável de contagem de referência que
guarda quantas referências apontam para o
objeto em questão. Quando esse contador chega
a 0, então a memória é liberada.

Uma forma de nós mesmos verificarmos isso pode
ser feita dessa forma:

import sys

a = []
b = a
print(sys.getrefcount(a))  # Retorna 3

Mas por que 3? Pois uma referência é o próprio
"a", outra é o "b" e por ultimo o argumento na
função getrefcount() do módulo sys.

Caso declarecemos que agora o "b" é None, então
teriamos que a contagem de referência é 2, sendo
1 do argumento da função + 1 do "a".

--------------------------------------------------

O problema gerado com esse recurso também vem do
fato de que o Reference Counting precisa de uma
proteção contra o fenômeno 'Race Conditions', que
ocorre quando duas threads aumentam ou diminuem
seu valor simultaneamente.

Quando isso acontece, poderá causar problemas como
a memória nunca ser liberada, ou pior, a memória
ser liberada quando ainda há objetos que apontam
para aquele espaço. Esse evento causa 'crashs' em
nossos sistemas.

Este reference couting pode ser mantido seguro
adicionando 'locks' emtoda estruturadedados que
são compartilhadas via threads. Desta forma eles
não são modificados deformainconsistente.

O problema é que adicionar 'locks' em cada objeto
ou grupo de objetos significa que múltiplos locks
irão existir, e isso irá causar um outro problema
- Deadlocks (deadlocks só podem existir se existe
mais de um lock). Outro efeito colateral seria
decaimento da performance causada pela repetida
aquisição e liberação dos locks.

O GIL aplica na regra de execução de qualquer código
Python o single lock previnindo qualquer deadlock, o
que por outro lado transforma qualquer código Python
emsingle-thread.

Vale mencionar que o GIL apesar de ser usado também em
outras linguagens de programação,como Ruby, não é a
única solução.

Algumas linguagens evitam o uso do GIL para gerenciamento
de memória em thread utilizando abordagens diferentes do
reference counting que o Python utiliza. Por exemplo, uma
das abordagens que outras linguagens utilizamé o compilador
JIT- Just in Time, como o Java.

-------------------------------------------------------------

Agora, um exemplo sobre o impacto em programas multi-tread.

Antes de tudo, veremos o desempenho single-thread:

<VÁ PARA O ARQUIVO single_thread.py no diretório multi_thread_multi_processing>

E então, o desempenho com multi-thread:

<VÁ PARA O ARQUIVO multi_thread.py no diretório multi_thread_multi_processing>

Quando vemos os resultados de tempo de execução dos
programas, reparamos que sua diferença é mínima, praticamente
iguais:

- Single-Thread: 2.2310030460357666 segundos
- Multi-Thread: 2.125131607055664 segundos

Isso acontece justamente por causa do GIL.

Então, COMO LIDAR COM GIL?

Uma solução seria, em vez de utilizar multithreading,
seria implementar o multi-processing.

Utilizando processos ao invés de threads, cada processo
Python ganha seu próprio interpretador Python e espaço
em memória. Desta forma, o GIl não será mais problema.

Façamos um exemplo de multi-processing então:

<VÁ PARA O ARQUIVO multi_processing.py no diretório multi_thread_multi_processing>

Com essa implementação de multi-processing, temos o
resultado em:

- 1.1588284969329834 segundos.

Praticamente o dobro de velocidade.

ATENÇÃO: Que fique claro que multi-processing são mais
'pesados' que multi-threading. Ou seja, lembre-se que
para cada processo, teremos um ambiente Python próprio.

------------------------------------------------------------------

Chegamos agora aos interpretadores alternativos de Python:

Conforme mencionado antes, Python possui múltiplas
implementações, dentre as principais: CPython (que
é a padrão, a que todos utilizamos), Jython, IronPython
e PyPy, escritos em C, Java, C# e Python respectivamente.

GIL só existe na implementação original (CPython).
Então se seu programa estiver rodando em outra
implementação, você não terá o problema que o GIL traz.
"""
