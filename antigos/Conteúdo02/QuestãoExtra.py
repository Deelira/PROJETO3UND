'''Desenvolva um algoritmo que ajude o professor a ler o nome e nota da prova dos 55 alunos do p1.
O algoritmo deve verificar a menor, a maior e a media das notas. Ele tambem deve aumentar 1 ponto
para os alunos que ficaram com nota abaixo de 5.
'''

maior = 0
menor = 10
soma = 0


for i in range(55):
    nome = input('Digite seu nome: ')
    nota = float('Digite sua nota: ')
    
    if nota < menor:
        menor = nota
    
    if nota > maior:
        maior = nota

    if nota < 5:
        nota += 1

    soma = soma + nota

media = soma / 55

print(f'A maior nota da turma foi {maior}, já a menor nota foi {menor}. A média de todas as notas é {media}')