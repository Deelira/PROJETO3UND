'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
utilizados são:
'''

eleitores = 1
Candidato1 = 0
Candidato2 = 0
Candidato3 = 0
Candidato4 = 0
Nulos = 0
Brancos = 0
voto = 1
contagem = 0

while voto != 0:
    print('1 - Candidato1 \n2 - Candidato2\n3 - Candidato3\n4 - Candidato4\n5 - Nulo\n6 - Voto em Branco')
    voto = int(input('Em quem deseja votar? '))
    if voto == 1:
        Candidato1 += 1
    if voto == 2:
        Candidato2 += 1
    if voto == 3:
        Candidato3 += 1
    if voto == 4:
        Candidato4 += 1
    if voto == 5:
        Nulos += 1
    if voto == 6:
        Brancos += 1
    contagem += 1

print(f'O candidato Candidato1 recebeu {Candidato1} voto(s).')
print(f'O candidato Candidato2 recebeu {Candidato2} voto(s).')
print(f'O candidato Candidato3 recebeu {Candidato3} voto(s).')
print(f'O candidato Candidato4 recebeu {Candidato4} voto(s).')
print(f'Houveram {Nulos} voto(s) nulos')
print(f'Houveram {Brancos} voto(s) em branco')
print(f'A percentagem de nulos é de {(Nulos/contagem) * 100:.2f} %')
print(f'A percentagem de brancos é de {(Brancos/contagem) * 100:.2f} %')