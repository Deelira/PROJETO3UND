'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio 
gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

'''

total = 0
qnt_cds = 0
media = 0

qnt_cds = int(input('Digite a quantidade de CDs:  '))

for i in range (1, qnt_cds + 1):
    valor = float(input(f'Qual o valor do {i}º CD? '))
    total += valor

media = total / qnt_cds

print(f'Você investiu o total de R$ {total:.2f} em seus CDs ')
print(f'A média de valor dos CDs é de R$ {media:.2f} ')
