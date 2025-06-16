'''
. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
outro valor deve aparecer valor inválido.

'''

dia = int(input('Digite o número correspondente: '))

if dia > 0:
    if dia == 1:
        dia = 'Domingo'
    elif dia == 2:
        dia = 'Segunda'
    elif dia == 3:
        dia = 'Terça'
    elif dia == 4:
        dia = 'Quarta'
    elif dia == 5:
        dia = 'Quinta'
    elif dia == 6:
        dia = 'Sexta'
    elif dia == 7:
        dia = 'Sábado'

    print(f'O dia correspondente é {dia}')
else:
    print('Número inválido!')