'''
 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.
'''

prod1 = float(input('Digite o valor do produto: '))
prod2 = float(input('Digite o valor do outro produto: '))
prod3 = float(input('Digite o valor do outro produto: '))

if prod1 < prod2 and prod1 < prod3:
    print(f'Você deve comprar o primeiro produto, que custa {prod1}' )
elif prod2 < prod1 and prod2 < prod3:
    print(f'Você deve comprar o segundo produto, que custa {prod2}' )
elif prod3 < prod2 and prod3 < prod1:
    print(f'Você deve comprar o terceiro produto, que custa {prod3:.2f}' )
else:
    print('Os produtos possuem o mesmo valor, fica por sua escolha.')