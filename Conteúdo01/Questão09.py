'''
Faça um Programa que leia três números e mostre-os em ordem decrescente
'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    primeiro = num1
elif num1 > num2 and num1 < num3 or num1 > num3 and num1 < num2:
    segundo = num1
else:
    terceiro = num1

if num2 > num1 and num2 > num3:
    primeiro = num2
elif num2 > num1 and num2 < num3 or num2 > num3 and num2 < num1:
    segundo = num2
else:
    terceiro = num2

if num3 > num1 and num3 > num2:
    primeiro = num3
elif num3 > num1 and num3 < num2 or num3 > num2 and num3 < num1:
    segundo = num3
else:
    terceiro = num3

print(f'{primeiro:.2f}, {segundo:.2f}, {terceiro:.2f}')