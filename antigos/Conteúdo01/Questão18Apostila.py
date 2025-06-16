'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida
'''

data = input('Digite a data desejada no formato dd/mm/aaaa: ')

dia = int(data.split('/')[0])
mes = int(data.split('/')[1])
ano = int(data.split('/')[2])

if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano <= 2025:
    print('Data válida!')
else:
    print('Data inválida!')