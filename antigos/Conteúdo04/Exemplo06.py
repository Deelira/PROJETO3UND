'''
Faça um algorítmo que receba 5 nomes e verifique se algum nome se repete
'''

nomes = []
repetidos = []
total = 0

for i in range(1, 6):
    nome = input(f'Digite o {i}º nome: ').lower()
    nomes.append(nome)

for r in nomes:
    if nomes.count(r) >= 2 and r not in repetidos:
        repetidos.append(r)
       
for i in repetidos:
    total += 1

if total >= 2:
    print(f'Aqui está uma lista com os nomes repetidos: {repetidos}')
elif total == 1:
    print(f'Aqui está uma lista com o nome repetido: {repetidos}')
else:
    print('Não existem nomes repetidos')