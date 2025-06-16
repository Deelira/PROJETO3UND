'''
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos
'''
total = 0
qnt_alunos = 0
alunos = []
turma = []

turmas = int(input('Digite a quantidade de turmas: '))

for i in range (1, turmas + 1):
    qnt_alunos = int(input(f'Quantos alunos estão matriculados na turma {i}? '))
    alunos.append(qnt_alunos)
    total += qnt_alunos
    turma.append(i)

media = total / turmas

print(f'Temos o total de {turmas} turmas e {total} alunos matriculados', end=' ')
print(f'e a média de alunos matriculados em nossas turmas é {media:.0f}')

print (turma)
print (alunos)