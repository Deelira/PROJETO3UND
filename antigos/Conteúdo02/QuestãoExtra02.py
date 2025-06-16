'''A turma do p1 precisa eleger um representante de sala. A eleição contém apenas três candidatos para serem
votados pelos 55 alunos. Contrua um algoritmo em python para ler o nome dos 3 candidatos e receber os votos.
Exiba o candidato eleito ao final.
'''

candidato1 = input('Digite o nome do primeiro candidato: ')
candidato2 = input('Digite o nome do segundo candidato: ')
candidato3 = input('Digite o nome do terceiro candidato: ')
total_candidato1 = 0
total_candidato2 = 0
total_candidato3 = 0

for i in range(55):
    print(f'Os candidatos são: 1:{candidato1}, 2:{candidato2}, 3:{candidato3}.')
    voto = int(input(' Digite o número referente ao candidato que deseja votar: '))
  
    if voto == 1:
        total_candidato1 += 1

    elif voto == 2:
        total_candidato2 += 1

    elif voto == 3:
        total_candidato3 += 1

if total_candidato1 > total_candidato2 and total_candidato1 > total_candidato3:
    print(f'O candidato eleito foi {candidato1}')
elif total_candidato2 > total_candidato1 and total_candidato2 > total_candidato3:
    print(f'O candidato eleito foi {candidato2}')
elif total_candidato3 > total_candidato1 and total_candidato3 > total_candidato2:
    print(f'O candidato eleito foi {candidato2}')
elif total_candidato1 == total_candidato2:
    print(f'Eleição empatada entre os candidatos {candidato1} e {candidato2}')
elif total_candidato1 == total_candidato3:
    print(f'Eleição empatada entre os candidatos {candidato1} e {candidato3}')
elif total_candidato2 == total_candidato3:
    print(f'Eleição empatada entre os candidatos {candidato2} e {candidato3}')
elif total_candidato2 == total_candidato1:
    print(f'Eleição empatada entre os candidatos {candidato1} e {candidato2}')