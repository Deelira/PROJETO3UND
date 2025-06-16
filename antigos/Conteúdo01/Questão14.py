'''
 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
a sua média. A atribuição de conceitos obedece à tabela abaixo:

'''

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2) / 2

if media >= 9 and media <= 10:
    conceito = 'A'
elif media >= 7.5 and media < 9:
    conceito = 'B'
elif media >= 6 and media < 7.5:
    conceito = 'C'
elif media >= 4 and media < 6:
    conceito = 'D'
elif media < 4 and media >= 0:
    conceito = 'E'

print('')
print('Média de aproveitamento                  Conceito')
print(f'         {media}                                {conceito}')
print('')
print('')