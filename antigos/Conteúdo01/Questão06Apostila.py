#Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O maior número entre eles é primeiro, {n1:.2f}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número entre eles é o segundo, {n2:.2f}')
else:
    print(f'O maior número entre eles é o terceiro, {n3:.2f}')