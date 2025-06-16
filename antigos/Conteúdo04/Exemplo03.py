'''
Faça um sistema de votos para ler os 3400 votos dos eleitores
'''

candidatos = ['jose','maria','carla']
votos = [0,0,0]
eleitores = 0

while eleitores != 3399:
    voto = input('Em quem você deseja votar: (Jose), (Maria), (Carla) ').lower()

    if voto == 'jose':
        votos[0] += 1
    elif voto == 'maria':
        votos[1] += 1
    elif voto == 'carla':
        votos[2] += 1
    eleitores += 1
    
print(votos)

if votos[0] > votos[1] and votos[0] > votos[2]:
    print(f'O candidato eleito com maior número de votos foi {candidatos[0]}')
elif votos[1] > votos[2] and votos[1] > votos[0]:
    print(f'O candidato eleito com maior número de votos foi {candidatos[1]}')
elif votos[2] > votos[0] and votos[2] > votos[1]:
    print(f'O candidato eleito com maior número de votos foi {candidatos[2]}')
else:
    print('Houve um empate, haverá reeleição!')