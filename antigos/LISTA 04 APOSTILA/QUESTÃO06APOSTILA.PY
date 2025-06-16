'''
 Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima
o número de alunos com média maior ou igual a 7.0.
'''
nome_alunos = []
media_alunos = []
quantidade_aprovados = 0
soma = 0

for i in range (1):
    nome = input('Digite o nome do aluno: ')
    for n in range(1,5):
        nota = float(input(f'Digite sua {n}ª nota: '))
        soma = soma + nota

    media = soma / 4
    nome_alunos.append(nome)
    media_alunos.append(media)

for n, m in zip(nome_alunos, media_alunos):
    print(f'Aluno: {n} \n Media: {m}')

for media in media_alunos:
    if media >= 7:
        quantidade_aprovados += 1

print(f'A quantidade de aprovados foi {quantidade_aprovados}')