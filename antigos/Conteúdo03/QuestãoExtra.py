'''
desenvolva um algoritmo que leia o nome de todos os alunos que estiveram em sala hoje. O algoritmo deve para a 
leitura quando for digitado a palavra 'fim'. no final, diga quantos alunos estiveram em sala
'''

contador = 0
nome = ''

while nome != fim:
    nome = input('qual o nome do aluno(a): ')
    contador += 1

print(f'Estiveram presente em sala {contador} aluno(s)')