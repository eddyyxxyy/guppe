"""
29) Faça uma prova de matemática para crianças que estão aprendendo
a somar números inteiros menores do que 100. Escolha números aleatórios
entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b,
onde a e b são os números aleatórios. Peça a resposta. Faça cinco
perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou
"""
from random import randint
from collections import deque

a: int
b: int
acertos: int = 0
answer: int = 0
answers: deque = deque()
results: deque = deque()
print('-=' * 15 + '\n' + 'APRENDENDO A SOMAR'.center(30, '-') + '\n' + '=-' * 15)
while len(answers) < 5:
    a = randint(1, 100)
    b = randint(1, 100)
    try:
        answer = int(input(f'{len(answers) + 1} - Quanto é {a} + {b}?\n').strip())
    except ValueError:
        print(f'{answer} é inválido, tente novamente...\n')
        continue
    else:
        if answer < 2 or answer > 200:
            print(f'{answer} é inválido, tente novamente...\n')
            continue
        else:
            results.append(a + b)
            answers.append(answer)
for i in range(5):
    if results[i] == answers[i]:
        acertos += 1
print('-' * 30 + '\n' + f'Você acertou {acertos} questões!'.center(30))
print('-' * 30 + '\nGabarito:')
for i in range(5):
    print(f'Questão {i + 1} - {results[i]}'.ljust(17) + f'|  Sua resposta: {answers[i]}')
