# Dados o gabarito de uma prova de 5 questões, o número de alunos e os cartões resposta de cada um, imprima o número de acertos de cada um
gabarito = ['A','B','C','D','E']
n = int(input('digite o número de alunos '))
for i in range(n):
    respostas = ['A','B','C','D','E']
    print('digite as respostas: ')
    acertos = 0
    for j in range(len(respostas)):
        print(f'resposta questão {j}:')
        respostas[j] = input()
        if respostas[j] == gabarito[j]:
            acertos += 1
    print(f' aluno acertou {acertos}')