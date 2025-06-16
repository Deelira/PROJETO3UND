'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada 
eleitor votar e ao final mostrar o número de votos de cada candidato
'''

candidatos = ['candidato1', 'candidato2', 'candidato3']
votos = [0,0,0]
voto = 1

eleitores = int(input('Quantos eleitores irão votar? '))

for n in range (eleitores):
    for i in range (0,3):
        print(f'Digite {voto} para votar no {candidatos[i]}')
        voto += 1
    voto_final = int(input('Em quem você deseja votar? (1) (2) (3) '))
    if voto_final == 1:
        votos[0] += 1
    elif voto_final == 2:
        votos[1] += 1
    elif voto_final == 3:
        votos[2] += 1

print(candidatos)
print(votos)