'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
'''

saque = float(input('Digite o valor que deseja sacar: R$ '))

n100 = saque // 100
resto_100 = saque % 100
n50 = resto_100 // 50
resto_50 = resto_100 % 50
n10 = resto_50 // 10
resto_10 = resto_50 % 10
n5 = resto_10 // 5
resto_5 = resto_10 % 5
print(f'Serão necessárias {n100:.0f} nota(s) de cem, {n50:.0f} nota(s) de cinquenta, {n10:.0f} nota(s) de dez, {n5:.0f} nota(s) de cinco e {resto_5:.0f} nota(s) de um real.')