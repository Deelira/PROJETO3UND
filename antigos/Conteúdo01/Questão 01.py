#. Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('Digite o primeiro valor:'))
num2 = float(input('Digite o segundo valor:'))

if num1 > num2:
    print(f'O número maior é {num1} ')
if num1 == num2:
    print('Os números são iguais')
if num2 > num1:
    print(f'O número maior é {num2}')