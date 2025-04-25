'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
não bissexto
'''

ano = int(input('Digite o ano: '))

confirmacao = ano % 4

if confirmacao == 0:
    print('Este é um ano bissexto!')
else:
    print('Este não é um ano bissexto!')