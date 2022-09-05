"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real
sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das
lâmpadas da sua casa.


Classes podem conter:

    -> Atributos: Representam as características do objeto. Ou seja, pelos
    atributos conseguimos representar computacionalmente os estados de um objeto.
    No caso da lâmpada, possivelmente, iríamos querer saber se a lâmpada é 110V ou
    220V, se ela é branca, amarela, vermelha, etc, qual sua luminosidade e muito
    mais.

    -> Métodos (funções): representam os comportamentos do objeto, ou seja, as
    ações que este objeto pode realizar no seu sistema. No caso da lâmpada, por
    exemplo, um comportamento comum que muito provavelmente iriamos querer
    representar no nosso sistema é o de ligar e desligar a mesma.


Em Python, para definir uma classe utilizamos a palavra reservada "class".

OBS: Quando nomeamos nossas classes em Python, utilizamos por convenção o nome com
inicial em maiúsculo, se o nome for composto, utiliza-se as iniciais das palavras
em maíusculo, todas as palavras juntas.

DICA GEEK! -> Em computação, não utilizamos: Acentuação, caracteres especiais, espaços
ou similares para nomes de classes, atributos, métodos, arquivos, diretórios, etc!

OBS: quando estamos planejando um software e definimos quais classes temos de ter no
sistema, chamamos estes objetos que serão mapeados para classes de ENTIDADES.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


lamp = Lampada()

print(type(lamp))
