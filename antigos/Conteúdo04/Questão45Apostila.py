'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai
utilizar o sistema. Após todos os alunos terem respondido informar:
a. Maior e Menor Acerto;
b. Total de Alunos que utilizaram o sistema;
c. A Média das Notas da Turma.

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes
dos alunos usarem o programa.

'''

gabarito = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']
alunos = []
op = 's'

# OBTER NOTAS
while op != 'n':
    resposta = []
    nota = 0
    for i in range (10):
        questao = input(f'Digite a resposta da questão {i + 1}: ').lower()
        resposta.append(questao)
        if questao == gabarito[i]:
            print('Resposta correta!')
            nota += 1
        else:
            print('Que pena, resposta errada!')
    if nota >= 7 and nota <= 10:
        print(f'Parabéns, sua nota foi {nota} e você está APROVADO!')
    else:
        print(f'Que pena, sua nota foi {nota} e você está REPROVADO!')
    alunos = [resposta, nota]
    op = input('Deseja conferir outra prova? (S) (N)').lower()

# MAIOR E MENOR NÚMERO DE ACERTOS
total = 0
maior = 0
menor = 99

for aluno in alunos:
    if aluno[1] > maior:
        maior = aluno[1]
    elif aluno[1] < menor:
        menor = aluno[1]
    
    total += aluno[1]
media = total / len(alunos) 
print(f'{len(alunos)} utilizaram o sistema\n')
print(f'A média das notas é {media}')